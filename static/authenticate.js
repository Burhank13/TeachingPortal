document.getElementById('teacher-button').addEventListener('click',
function()
{
    document.querySelector('.bg-modal').style.display = 'flex';
});

document.getElementById('student-button').addEventListener('click',
function()
{
    document.querySelector('.bg-modal').style.display = 'flex';
});

document.querySelector('.close').addEventListener('click',
function(){
    document.querySelector('.bg-modal').style.display = 'none';
});

function goback(){
    window.history.back();
};