var skills = {};

window.onload = function() {
  var sliders = document.getElementsByClassName('slider');
  
  for (var i = 0; i != sliders.length; ++i) {      
    slider(sliders[i].value, i + 1);
  }
};

function slider(value, index) {
  id    = 'slider' + String(index);
  skill = 'skill'  + String(index);
  
  skills[id] = value;
  w3.displayObject(id, skills); // BADGE
  
  console.log(skill);
  
  var obj = {}
  obj[skill] = skill_value_to_level(value);
  
  // SKILL LEVEL
  w3.displayObject(skill, obj);

  // OVERALL PROFICIENCY
  calculate_proficiency();
}

function calculate_proficiency() {
  slider_values = 0;

  for (skill in skills) {
    if (!skills.hasOwnProperty(skill)) continue;
    slider_values += Number(skills[skill]);
  }
  
  w3.displayObject('role', {
    'role' : total_values_to_role(slider_values)
  });
}

function skill_value_to_level(value) {
  var proficiency = 'Novice';
  if (value == 10)     proficiency = 'Expert';
  else if (value >= 7) proficiency = 'Advanced';
  else if (value >= 4) proficiency = 'Intermediate';
  
  return proficiency;
}

function total_values_to_role(value) {
  var role = 'Entry-level'
  
  if (value >= 33)      role = 'Senior-level';
  else if (value >= 23) role = 'Junior-level';
  
  return role;
}
