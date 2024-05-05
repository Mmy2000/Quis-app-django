const modalBtn = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('startBtn')
const url = window.location.href
const url2 = window.location.href
const quizBox = document.getElementById('quizBox')
let data
modalBtn.forEach(modalBtn => modalBtn.addEventListener("click" , ()=>{
    const pk = modalBtn.getAttribute('data-pk')
    const name = modalBtn.getAttribute('data-quiz')
    const question = modalBtn.getAttribute('data-questions')
    const difficulty = modalBtn.getAttribute('data-difficulty')
    const time = modalBtn.getAttribute('data-time')
    const score = modalBtn.getAttribute('data-pass')
    console.log(name);
    modalBody.innerHTML = `<div class="mb-3">Are you sure you want to begin "<b>${name}</b>"?</div>
    <div class="text-muted">
    <ul>
    <li>Difficulty: <b>${difficulty}</b></li>
    <li>number of question: <b>${question}</b></li>
    <li>score to pass: <b>${score}%</b></li>
    <li>Time: <b>${time} min</b></li>
    </ul>
    </div>`
    startBtn.addEventListener('click' , ()=>{
        window.location.href = url + pk    })
}) 
    
);

// data auiz view


$.ajax({
    type: "GET",
    url: `${url}data`,
    success: function (response) {
        console.log(response);
        data = response.data
        data.forEach(el =>{
            for (const [question , answers] of Object.entries(el)) {
                console.log(question);
                console.log(answers);
            }
        })
    },
    error:function(error){
        console.log(error);
    }
});