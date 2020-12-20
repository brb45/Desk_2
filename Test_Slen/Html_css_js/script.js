    
var list = document.createElement('ul');
var info = document.createElement('p');
var html = document.querySelector('html');

info.textContent = 'Active Setup';

document.body.appendChild(info);
document.body.appendChild(list);

html.onclick = function() {
  var listItem = document.createElement('li');
  var listContent = prompt('What content do you want the list item to have?');
  listItem.textContent = listContent;
  list.appendChild(listItem);

  listItem.onclick = function(e) {
    e.stopPropagation();
    var listContent = prompt('Enter new content for your list item');
    this.textContent = listContent;
  }
}
 
