var skills = {}

window.addEventListener('load', () => {
    var value1 = valid_slider(localStorage.getItem('slider1'));
    var value2 = valid_slider(localStorage.getItem('slider2'));
    var value3 = valid_slider(localStorage.getItem('slider3'));
    var value4 = valid_slider(localStorage.getItem('slider4'));
    var value5 = valid_slider(localStorage.getItem('slider5'));

    skills = {
        sliders: {
            'slider1': [value1, value_to_proficiency(value1)],
            'slider2': [value2, value_to_proficiency(value2)],
            'slider3': [value3, value_to_proficiency(value3)],
            'slider4': [value4, value_to_proficiency(value4)],
        }
    }

    Object.defineProperty(skills, 'total', {
        get() {
            total = 0;
            for (let key in this.sliders)
                total += parseInt(this.sliders[key][0]);
            return total;
        }
    });

    Array.from(document.getElementsByClassName('slider')).forEach((elem, i) => {
        elem.value = skills.sliders['slider' + (i + 1)][0];
        slider(elem.value, i + 1);
    });
});


function valid_slider(value) {
    for (let i = 1; i <= 5; ++i)
        if (value == i) return value;
    return 1; // default value
}


//   0-3 years -- [0, 1, 2, 3]
//   4-7 years -- [4, 5, 6, 7]
//  8-11 years -- [8, 9, 10, 11]
// 12-15 years -- [12, 13, 14, 15]
//   >15 years -- [15...]
function value_to_proficiency(value) {
  var proficiency = 'Novice';

  switch (value) {
  case '5': proficiency = 'Master';       break;
  case '4': proficiency = 'Expert';       break;
  case '3': proficiency = 'Advanced';     break;
  case '2': proficiency = 'Intermediate'; break;
  case '1':
  default: break;
  }

  return proficiency;
}


// positions start at 1
function slider(value, position) {
  var sliderId      = 'slider'      + position;
  var valueId       = 'value'       + position;
  var proficiencyId = 'proficiency' + position;

  // VALUE; i.e., 1-5
  skills.sliders[sliderId][0] = value;   // store into the JS global
  localStorage.setItem(sliderId, value); // persists between sessions
  w3.displayObject(valueId, {[valueId]: value_to_years(value)});

  // PROFICIENCY; e.g., Novice
  skills.sliders[sliderId][1] = value_to_proficiency(value);
  w3.displayObject(proficiencyId, {[proficiencyId]: skills.sliders[sliderId][1]});

  // ROLE; e.g., Entry-level
  w3.displayObject('role', {'role': values_to_role(skills.total)});
}


// 1 --   0-3 years
// 2 --   4-7 years
// 3 --  8-11 years
// 4 -- 12-15 years
// 5 --   >15 years
function value_to_years(value) {
    var years = '0–3';

    switch (value) {
    case '5': years =   '>15'; break;
    case '4': years = '12–15'; break;
    case '3': years =  '8-11'; break;
    case '2': years =   '4-7'; break;
    case '1':
    default: break;
    }

    return years;
}


function values_to_role(total) {
  // max possible is 20
  var role = 'Entry-level';

  if      (total >= 16) role = 'Senior-level';
  else if (total >= 10) role = 'Junior-level';

  return role;
}
