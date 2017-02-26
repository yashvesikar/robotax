var stepTwo = false
var formStr = '<form><input type="text" name="numberOfEmployees" id="num-emp" class="" placeholder="# Employee" required><input type="text" name="averageTax" id="avg-tax" class="" placeholder="Average Tax" required><input type="text" name="wage" id="wage" class="" placeholder="Wage" required><input type="text" name="productivity" id="num-emp" class="" placeholder="Productivity" required></form>'

function setKeyUps() {
  $('#employee-add form').last().children().keyup(function() {
    complete_info = true;
    $.each($('#employee-add form').last().children(), function(index, value) {
      if ($(value).val().length == 0) {
        complete_info = false;
      }
    })
    if (complete_info == true) {

      $('#employee-add').append(formStr);
      setKeyUps();

      if (stepTwo == false) {
        stepTwo == true;
        $('#second-step h3').fadeIn('slow', function() {
          $('#new-emp-add').fadeIn('slow');
        });
        setStepTwoKeyUps()
      }
    }
  })
}

function setStepTwoKeyUps() {

}


setKeyUps();
