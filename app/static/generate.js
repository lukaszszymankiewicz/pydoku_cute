$(function() {
  $("#generation_button").click(function(event) {
    var difficult = $('form').serialize();

    $.getJSON('/generate_new_puzzle', {difficult}, function(data) {});

    var suffix = getRandomSuffix();
    document.getElementById("solved_sudoku").src = getSudokuPath(solvedSudokuPath, suffix);
    document.getElementById("unsolved_sudoku").src = getSudokuPath(unsolvedSudokuPath, suffix);

    return false;
  });
});

function getRandomSuffix(){
  return performance.now().toString();
}

function getSudokuPath(path, suffix) {
   return path.concat(suffix);
}
