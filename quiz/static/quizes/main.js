console.log('hello world');

const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('start-button')
const url = window.location.href

modalBtns.forEach(modalBtn=>modalBtn.addEventListener('click', ()=>{
    const pk = modalBtn.getAttribute('data-pk')
    const name = modalBtn.getAttribute('data-quiz')
    const number_of_questions = modalBtn.getAttribute('data-questions')
    const difficulty = modalBtn.getAttribute('data-difficulty')
    const score_to_pass = modalBtn.getAttribute('data-pass')

    modalBody.innerHTML = `
        <div class="h5 mb-3">Test your knowledge "<b>${name}</b>"?</div>
        <div class="text-muted">
            <ul>
                <li>difficulty: <b>${difficulty}</b></li>
                <li>number of questions: <b>${number_of_questions}</b></li>
                <li>score_to_pass: <b>${score_to_pass}</b></li>
            </ul>
        </div>
    `

    startBtn.addEventListener('click', ()=>{
        window.location.href = url + pk

    })
}))
