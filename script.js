const cells = document.querySelectorAll('[data-cell]');
const winnerMessage = document.getElementById('winnerMessage');
const winnerText = document.getElementById('winner');
const restartButton = document.getElementById('restartButton');

let isCircleTurn = false;

// Winning combinations
const WINNING_COMBINATIONS = [
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8],
  [0, 3, 6],
  [1, 4, 7],
  [2, 5, 8],
  [0, 4, 8],
  [2, 4, 6],
];

function handleClick(e) {
  const cell = e.target;
  const currentClass = isCircleTurn ? '0' : 'x';

  // Place the mark
  cell.textContent = currentClass;
  cell.classList.add('taken');

  // Check for a winner
  if (checkWin(currentClass)) {
    winnerMessage.style.display = 'block';
    winnerText.textContent = currentClass;
    return;
  }

  // Switch turns
  isCircleTurn = !isCircleTurn;
}

function checkWin(currentClass) {
  return WINNING_COMBINATIONS.some(combination => {
    return combinations.every(index => {
      return cells[index].textContent === currentClass;
    });
  });
}
