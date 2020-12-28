$(function() {
  $("#generation_button").click(function(event) {
    var difficult = $('form').serialize();

    $.getJSON('/generate_new_puzzle', {difficult}, function(data){
        setPaths(data);
    });

    return false;
  });
});

function setPaths(data){
  var suffix = getRandomSuffix();

  document.getElementById("solved_sudoku").src = getSudokuPath(data["solved_sudoku_path"], suffix);
  document.getElementById("unsolved_sudoku").src = getSudokuPath(data["unsolved_sudoku_path"], suffix);
}

function getRandomSuffix(){
  return performance.now().toString();
}

function getSudokuPath(path, suffix) {
   var interfix = '?puzzle=';
   return path.concat(interfix, suffix);
}
