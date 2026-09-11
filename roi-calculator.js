/**
 * Volo AI — ROI Calculator
 * Updates the ROI card values when the user changes inputs.
 */
(function () {
  var callsInput = document.getElementById('roi-calls');
  var valueInput = document.getElementById('roi-value');
  var perWeekEl = document.getElementById('roi-per-week');
  var perMonthEl = document.getElementById('roi-per-month');
  var breakevenEl = document.getElementById('roi-breakeven');

  function fmt(n) {
    return '£' + Math.round(n).toLocaleString('en-GB');
  }

  function update() {
    var calls = parseInt(callsInput.value, 10) || 0;
    var value = parseInt(valueInput.value, 10) || 0;
    var weekly = calls * value;
    var monthly = weekly * 4.33;
    perWeekEl.textContent = fmt(weekly);
    perMonthEl.textContent = fmt(monthly);
    if (value > 0) {
      var be = Math.ceil(29 / value);
      breakevenEl.textContent = be;
    } else {
      breakevenEl.textContent = '—';
    }
  }

  if (callsInput && valueInput) {
    callsInput.addEventListener('input', update);
    valueInput.addEventListener('input', update);
    update();
  }
})();
