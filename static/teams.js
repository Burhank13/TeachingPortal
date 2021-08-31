function profileDropdown() {
    document.getElementById("profile-dropdown-menu").classList.toggle("show");
  }
 
  // Close the dropdown menu if the user clicks outside of it
  window.onclick = function(event) {
    if (!event.target.matches('.dropdown_button')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }

document.getElementById('join-button').addEventListener('click',
function()
{
    document.querySelector('.join-bg-modal').style.display = 'flex';
});

document.getElementById('create-button').addEventListener('click',
function()
{
    document.querySelector('.create-bg-modal').style.display = 'flex';
});

document.getElementById('student-button').addEventListener('click',
function()
{
    document.querySelector('.bg-modal').style.display = 'flex';
});

document.querySelector('.join-close').addEventListener('click',
function(){
    document.querySelector('.join-bg-modal').style.display = 'none';
    
});

document.querySelector('.create-close').addEventListener('click',
function(){
    document.querySelector('.create-bg-modal').style.display = 'none';
    
});

document.querySelector('.close-option').addEventListener('click',
function(){
    document.querySelector('.bg-modal').style.display = 'none';
    
});
