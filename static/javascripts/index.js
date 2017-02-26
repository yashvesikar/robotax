var stepTwo = false
var stepThree = false
var stepSubmit = false
var formStr = '<form><input type="text" name="numberOfEmployees" id="num-emp" class="" placeholder="# Employee" required><input type="text" name="averageTax" id="avg-tax" class="" placeholder="Average Tax" required><input type="text" name="wage" id="wage" class="" placeholder="Wage" required><input type="text" name="productivity" id="num-emp" class="" placeholder="Productivity" required></form>'
var step2FormStr = '<form id="step2form"><input type="text" name="numberOfEmployees" id="num-emp" class="" placeholder="# Employee" required><input type="text" name="averageTax" id="avg-tax" class="" placeholder="Average Tax" required><input type="text" name="wage" id="wage" class="" placeholder="Wage" required>'
var step3FormStr = '<form id="step3form"><input type="text" name="numberOfAutomations" id="num-auto" class="" placeholder="# Automations" required><input type="text" name="cost" id="cost" class="" placeholder="Cost" required><input type="text" name="productivity" id="productivity" class="" placeholder="Productivity" required></form>'

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
  $('#new-emp-add form').last().children().keyup(function() {
    complete_info = true;
    $.each($('#new-emp-add form').last().children(), function(index, value) {
      if ($(value).val().length == 0) {
        complete_info = false;
      }
    })
    if (complete_info == true) {

      $('#new-emp-add').append(step2FormStr);
      setStepTwoKeyUps();

      if (stepThree == false) {
        stepThree == true;
        $('#third-step h3').fadeIn('slow', function() {
          $('#automation-add').fadeIn('slow');
        });
        setStepThreeKeyUps();
      }
    }
  });
};

function setStepThreeKeyUps() {
  $('#automation-add form').last().children().keyup(function() {
    complete_info = true;
    $.each($('#automation-add form').last().children(), function(index, value) {
      if ($(value).val().length == 0) {
        complete_info = false;
      }
    });
    if (complete_info == true) {

      $('#automation-add').append(step3FormStr);
      setStepThreeKeyUps();

      if (stepSubmit == false) {
        stepSubmit == true;
        $('#submit-step').fadeIn('slow');
      }
    }
  });
};

setKeyUps();

$("#submit").click(function(e) {
  e.preventDefault();
  submitData = {
    oldEmployees: [],
    newEmployees: [],
    automations: []
  }

  $.each($('#employee-add form'), function(index, value) {
    var data = JSON.stringify($(value).serializeArray());
    console.log()
    if ($($(value).children()[0]).val().length > 0) {
      submitData['oldEmployees'].push(data);
    }
  })

  $.each($('#new-emp-add form'), function(index, value) {
    var data = JSON.stringify($(value).serializeArray());
    if ($($(value).children()[0]).val().length > 0) {
      submitData['newEmployees'].push(data);
    }
  })

  $.each($('#automation-add form'), function(index, value) {
    var data = JSON.stringify($(value).serializeArray());
    if ($($(value).children()[0]).val().length > 0) {
      submitData['automations'].push(data);
    }
  })

  $.ajax({
    url: '/calculations',
    data: submitData,
    dataType: 'json',
    type: 'POST',
    success: function(response) {
      console.log(response);
    },
    error: function(error) {
      console.log(error);
    }
  });

  console.log(submitData);


  return false;
});
