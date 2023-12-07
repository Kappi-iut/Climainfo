const canvas = document.getElementById("tetrisCanvas");
const canvasNextPiece = document.getElementById("nextPieceCanvas");
const context = canvas.getContext("2d");

const ROWS = 20;
const COLUMNS = 10;
const BLOCK_SIZE = 30;

let currentPiece;
let currentPieceColor;

let nextPiece;
let nextPieceColor;

let nbScore = 0;
let vitesse = 450;
let phase = 0;

let isGamePaused = false;

let viteseInterval = setInterval(update, vitesse);
const pieces = [
    [[1, 1, 1, 1]],

    [[1,1,1,1,1,1,1,1,1,1],
     [1,1,1,1,1,1,1,1,1,1]],

    [[1, 1, 1],
        [0, 1, 0]],

    [[1, 1, 1],
        [1, 0, 0]],

    [[1, 1, 1],
        [0, 0, 1]],

    [[1, 1, 0],
        [0, 1, 1]],

    [[0, 1, 1],
        [1, 1, 0]]
];
const couleurs = [
    "#00F0F0",
    "#0000F0",
    "#f0a100",
    "#f0f000",
    "#00f000",
    "#a000f0",
    "#f00000"
];


const board = [];
for (let row = 0; row < ROWS; row++) {
    board[row] = [];
    for (let col = 0; col < COLUMNS; col++) {
        board[row][col] = 0;
    }
}

function drawSquare(x, y, color) {
    context.fillStyle = color;
    context.fillRect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE);
    context.strokeStyle = "#000";
    context.strokeRect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE);
}
function drawBoard() {
    for (let row = 0; row < ROWS; row++) {
        for (let col = 0; col < COLUMNS; col++) {
            if (board[row][col] !== 0) {
                drawSquare(col, row, board[row][col]);
            }
        }
    }
}
function drawNextPiece() {
    const nextPieceCanvasContext = canvasNextPiece.getContext("2d");
    nextPieceCanvasContext.clearRect(0, 0, canvasNextPiece.width, canvasNextPiece.height);

    const blockSize = Math.min(
        canvasNextPiece.width / nextPiece[0].length,
        canvasNextPiece.height / nextPiece.length
    );

    const pieceWidth = nextPiece[0].length * blockSize;
    const pieceHeight = nextPiece.length * blockSize;

    const x = (canvasNextPiece.width - pieceWidth) / 2;
    const y = (canvasNextPiece.height - pieceHeight) / 2;

    for (let row = 0; row < nextPiece.length; row++) {
        for (let col = 0; col < nextPiece[row].length; col++) {
            if (nextPiece[row][col] !== 0) {
                const drawX = x + col * blockSize;
                const drawY = y + row * blockSize;
                nextPieceCanvasContext.fillStyle = nextPieceColor;
                nextPieceCanvasContext.fillRect(drawX, drawY, blockSize, blockSize);
                nextPieceCanvasContext.strokeStyle = "#000";
                nextPieceCanvasContext.strokeRect(drawX, drawY, blockSize, blockSize);
            }
        }
    }
}

function generatePiece() {
    const randomIndex = Math.floor(Math.random() * pieces.length);
    const randomColor = Math.floor(Math.random() * couleurs.length);
    currentPiece = pieces[randomIndex];
    currentPieceColor = couleurs[randomColor];
}
function generateNextPiece() {
    const randomIndex = Math.floor(Math.random() * pieces.length);
    const randomColor = Math.floor(Math.random() * couleurs.length);
    nextPiece = pieces[randomIndex];
    nextPieceColor = couleurs[randomColor];
}
function spawnPiece() {
    if(!nextPiece) {
        const randomIndex = Math.floor(Math.random() * pieces.length);
        const randomColor = Math.floor(Math.random() * couleurs.length);
        currentPiece = pieces[randomIndex];
        currentPieceColor = couleurs[randomColor];
        // Initial position of the piece
        currentPiece.x = Math.floor((COLUMNS - currentPiece[0].length) / 2);
        currentPiece.y = 0;
    }else {
        currentPiece = nextPiece;
        currentPieceColor = nextPieceColor;
        // Initial position of the piece
        currentPiece.x = Math.floor((COLUMNS - currentPiece[0].length) / 2);
        currentPiece.y = 0;
    }
    generateNextPiece();
}
function canMove(piece, offsetX, offsetY) {
    for (let row = 0; row < piece.length; row++) {
        for (let col = 0; col < piece[row].length; col++) {
            if (piece[row][col] !== 0) {
                const newX = currentPiece.x + col + offsetX;
                const newY = currentPiece.y + row + offsetY;

                if (newX < 0 || newX >= COLUMNS || newY >= ROWS || board[newY][newX] !== 0) {
                    return false;
                }
            }
        }
    }
    return true;
}
function mergePiece() {
    for (let row = 0; row < currentPiece.length; row++) {
        for (let col = 0; col < currentPiece[row].length; col++) {
            if (currentPiece[row][col] !== 0) {
                const boardX = currentPiece.x + col;
                const boardY = currentPiece.y + row;
                board[boardY][boardX] = currentPieceColor;
            }
        }
    }
    // Check if the merged piece has reached the top of the board
    if (currentPiece.y <= 0) {
        clearInterval(update);
        displayMessage("Défaite... mais félicitations, vous avez perdu votre temps !");
        isGamePaused = true;
    }
    spawnPiece();
}
function resetGame() {
    window.location.reload();
    // Reset the board
    for (let row = 0; row < ROWS; row++) {
        for (let col = 0; col < COLUMNS; col++) {
            board[row][col] = 0;
        }
    }
    spawnPiece();
}

function rotatePiece() {
    const originalPiece = currentPiece;
    let x = currentPiece.x;
    let y = currentPiece.y;
    currentPiece = currentPiece[0].map((_, i) => currentPiece.map(row => row[i]));
    currentPiece.reverse();
    currentPiece.x = x;
    currentPiece.y = y;
    if (!canMove(currentPiece, 0, 0)) {
        currentPiece = originalPiece; // Revert the rotation if it's not valid
    }
}
function movePiece(dirX, dirY) {
    if (canMove(currentPiece, dirX, dirY)) {
        currentPiece.x += dirX;
        currentPiece.y += dirY;
    } else if (dirY !== 0) {
        mergePiece();
    }
}
function clearRows() {
    let rowsCleared = 0;
    for (let row = ROWS - 1; row >= 0; row--) {
        if (board[row].every(cell => cell !== 0)) {
            board.splice(row, 1);
            board.unshift(Array(COLUMNS).fill(0));
            rowsCleared++;
        }
    }

    if (rowsCleared > 0) {
        const points = Math.pow(2, rowsCleared - 1) * 15;
        nbScore += points;
        if(nbScore>404){
            nbScore = 404;
            document.getElementById("score").innerText = "Score: " + nbScore;
            clearInterval(update);
            displayMessage("Félicitations, vous avez perdu votre temps !");
            isGamePaused = true;
        }
        document.getElementById("level").innerText = "Level: " + phase;
        document.getElementById("score").innerText = "Score: " + nbScore;
        if(nbScore/16 > phase) {
            phase = Math.floor(nbScore/16);
            vitesse = 450 + phase*15;
            clearInterval(viteseInterval);
            viteseInterval = setInterval(update, vitesse);
        }
    }
}
function draw() {
    context.clearRect(0, 0, canvas.width, canvas.height);
    drawBoard();
    drawPiece();
    drawNextPiece();
}
function drawPiece() {
    for (let row = 0; row < currentPiece.length; row++) {
        for (let col = 0; col < currentPiece[row].length; col++) {
            if (currentPiece[row][col] !== 0) {
                drawSquare(currentPiece.x + col, currentPiece.y + row, currentPieceColor);
            }
        }
    }
}
function update() {
    if (isGamePaused) {
        return;
    }
    console.log(vitesse);
    movePiece(0, 1);
    gameLoop();

}
function gameLoop() {
    if (isGamePaused) {
        return;
    }
    draw();
}

document.addEventListener("keydown", function(event) {
    if (event.key === "a" || event.key === "A") {
        rotatePiece();
        gameLoop();
    } else if (event.key === "ArrowLeft") {
        movePiece(-1, 0);
        gameLoop();
    } else if (event.key === "ArrowRight") {
        movePiece(1, 0);
        gameLoop();
    } else if (event.key === "ArrowDown") {
        movePiece(0, 1);
        gameLoop();
    }
});

function displayMessage(message) {
    const gameMessage = document.getElementById("gameMessage");
    const gameMessageText = document.getElementById("gameMessageText");
    gameMessageText.innerText = message;
    gameMessage.classList.remove("hidden");
    console.log(message);
}

generatePiece();
spawnPiece();

setInterval(clearRows, 0.1);