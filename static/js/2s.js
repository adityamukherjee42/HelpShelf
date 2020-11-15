function addItem() {
  let item = document.getElementById('task').value;
  let day = document.getElementById('days').value;
  let newItem = document.createElement('li');
  /*
    This is an adaption of the to-do-list I made a couple of days ago. I wanted to make the checkboxes disappear and only appear when hovered upon, but i was
    unable to get it to work. I got it to work for one but when you hover over the other items it would show the first items checkbox and not its checkbox. Still working the bugs out on that part. Hope you guys like the planner.
    
    Any suggestions for improvements is welcome :)
  */
  
  let checkbox = document.createElement('input');
  let newLine = document.createElement('br');
  newItem.setAttribute('class','list-item')
  checkbox.setAttribute('type','checkbox');
  checkbox.setAttribute('id','check-box');
  newItem.textContent = item;
  if (day == 'monday') {
    document.getElementById('monday').appendChild(newItem);
    document.getElementById('monday').appendChild(checkbox);
    document.getElementById('monday').appendChild(newLine);
  } else if (day == 'tuesday'){
    document.getElementById('tuesday').appendChild(newItem);
    document.getElementById('tuesday').appendChild(checkbox);
    document.getElementById('tuesday').appendChild(newLine);
  }else if (day == 'wednesday') {
    document.getElementById('wednesday').appendChild(newItem);
    document.getElementById('wednesday').appendChild(checkbox);
    document.getElementById('wednesday').appendChild(newLine);
  } else if (day == 'thursday') {
    document.getElementById('thursday').appendChild(newItem);
    document.getElementById('thursday').appendChild(checkbox);
    document.getElementById('thursday').appendChild(newLine);
  } else if (day == 'friday') {
    document.getElementById('friday').appendChild(newItem);
    document.getElementById('friday').appendChild(checkbox);
    document.getElementById('friday').appendChild(newLine);
  } else if (day == 'saturday') {
    document.getElementById('saturday').appendChild(newItem);
    document.getElementById('saturday').appendChild(checkbox);
    document.getElementById('saturday').appendChild(newLine);
  } else if (day == 'sunday') {
    document.getElementById('sunday').appendChild(newItem);
    document.getElementById('sunday').appendChild(checkbox);
    document.getElementById('sunday').appendChild(newLine);
  }
  document.getElementById('task').value = "";
}

function popOffItem() {
  let checked_list = document.querySelectorAll('#check-box');
  let checked_list_item = document.querySelectorAll('.list-item');
  let lineBreaks = document.querySelectorAll('br');
  for (i=0; i < checked_list.length; i++) {
    if (checked_list[i].checked==true) {    
      //Removing the Item from the Document
      let checkbox_elemt = checked_list[i];
      let item = checked_list_item[i];
      let removeBreakLine = lineBreaks[i];
      let parent1 = checkbox_elemt.parentNode;
      let parent2 = item.parentNode;
      let parent3 = removeBreakLine.parentNode;
      parent1.removeChild(checkbox_elemt);
      parent2.removeChild(item);
      parent3.removeChild(removeBreakLine);
    }else {
      continue;
    }
  }
}