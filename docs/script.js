let board = [1, 2, 3, 4, 5, 6, 7, 8, 0];
let initialBoard = [...board];
const boardElement = document.getElementById('board');

function initGame() {
    renderBoard();
    document.getElementById('scramble-btn').onclick = scramble;
    document.getElementById('reset-btn').onclick = reset;
}

function renderBoard() {
    boardElement.innerHTML = '';
    board.forEach((value, index) => {
        const tile = document.createElement('div');
        tile.classList.add('tile');
        if (value === 0) {
            tile.classList.add('empty');
            tile.innerText = '';
        } else {
            tile.innerText = value;
            tile.onclick = () => handleTileClick(index);
        }
        boardElement.appendChild(tile);
    });
}

function handleTileClick(index) {
    const zeroIndex = board.indexOf(0);
    if (getValidMoves(zeroIndex).includes(index)) {
        swap(index, zeroIndex);
        renderBoard();
        if (isSolved()) document.getElementById('status').innerText = "Solved! 🎉";
    }
}

function getValidMoves(i) {
    const r = Math.floor(i / 3);
    const c = i % 3;
    const moves = [];
    const adj = [[r, c+1], [r, c-1], [r+1, c], [r-1, c]];
    
    adj.forEach(([nr, nc]) => {
        if (nr >= 0 && nr < 3 && nc >= 0 && nc < 3) {
            moves.push(nr * 3 + nc);
        }
    });
    return moves;
}

function swap(idx1, idx2) {
    [board[idx1], board[idx2]] = [board[idx2], board[idx1]];
}

function isSolvable(arr) {
    let inversions = 0;
    const flat = arr.filter(n => n !== 0);
    for (let i = 0; i < flat.length; i++) {
        for (let j = i + 1; j < flat.length; j++) {
            if (flat[i] > flat[j]) inversions++;
        }
    }
    return inversions % 2 === 0;
}

function scramble() {
    document.getElementById('status').innerText = "";
    let newBoard = [...board];
    do {
        newBoard.sort(() => Math.random() - 0.5);
    } while (!isSolvable(newBoard) || isSolved(newBoard));
    
    board = newBoard;
    initialBoard = [...newBoard];
    renderBoard();
}

function reset() {
    board = [...initialBoard];
    renderBoard();
}

function isSolved() {
    return board.every((val, i) => val === (i === 8 ? 0 : i + 1));
}

initGame();