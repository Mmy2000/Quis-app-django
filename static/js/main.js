const modalBtn = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('startBtn')
const url = window.location.href

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
const url2 = window.location.href
const quizBox = document.getElementById('quizBox')
const quizForm = document.getElementById('quiz-form')
const csrf = document.querySelector('[name=csrfmiddlewaretoken]')

console.log('csrf' + csrf.value);
$.ajax({
    type: "GET",
    url: `${url}data`,
    success: function (response) {
        console.log(response);
        const data = response.data
        data.forEach(el =>{
            for (const [question , answers] of Object.entries(el)) {
                quizBox.innerHTML += `
                    <hr>
                    <div class="mb-3">
                        <b>${question}</b>
                    </div>
                `
                answers.forEach(answer => {
                    quizBox.innerHTML += `
                        <div>
                            <input type="radio" class="ans" id="${question}-${answer}" name="${question}" value="${answer}">
                            <label for="${question}">${answer}</label>
                        </div>
                    `
                });
            }
        })
    },
    error:function(error){
        console.log(error);
    }
});

const sendData = () =>{
    const elements = [...document.getElementsByClassName('ans')]
    const data = {}
    data['csrfmiddlewaretoken'] = csrf.value
    elements.forEach(el=>{
        if (el.checked) {
            data[el.name] = el.value
        } else{
            if (!data[el.name]) {
                data[el.name] = null
            }
        }
    })
    $.ajax({
        type:"POST",
        url:`${url2}save/`,
        data:data,
        success:function(response){
            console.log(response);
        },
        error:function(error){
            console.log(error);
        }
    })
}

quizForm.addEventListener('submit' , e=>{
    e.preventDefault()
    sendData()
})