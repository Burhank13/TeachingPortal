
document.getElementById('teacher-button').addEventListener('click',
function()
{
    document.querySelector('.teacher-modal').style.display = 'flex';
});

document.getElementById('student-button').addEventListener('click',
function()
{
    document.querySelector('.student-modal').style.display = 'flex';
});

document.querySelector('.student-close').addEventListener('click',
function(){
    document.querySelector('.student-modal').style.display = 'none';
});

document.querySelector('.teacher-close').addEventListener('click',
function(){
    document.querySelector('.teacher-modal').style.display = 'none';
});

function goback(){
    window.history.back();
};

