document.addEventListener("DOMContentLoaded", () => {
    console.log("Script loaded!"); // for errors
    const modalBtns = [...document.getElementsByClassName('modal-button')]
    const modalBody = document.getElementById('modal-body-confirm')
    const startBtn = document.getElementById('start-button')

    const url =  window.location.href

    console.log("Found modal buttons:", modalBtns);

    modalBtns.forEach(modalBtn =>
        modalBtn.addEventListener('click', () => {
            const pk = modalBtn.getAttribute('data-pk')
            const name = modalBtn.getAttribute('data-quiz')
            const numQuestions = modalBtn.getAttribute('data-questions')
            const difficulty = modalBtn.getAttribute('data-difficulty')
            const scoreToPass = modalBtn.getAttribute('data-pass')

            modalBody.innerHTML = `
                <div class="h5 mb-3">Enjoy "<b>${name}</b>"</div>
                <div class="text-muted">
                    <ul>
                        <il>difficulty: <b>${difficulty}</b></il> <br>
                        <il>number of questions: <b>${numQuestions}</b></il> <br>
                        <il>score to pass: <b>${scoreToPass}%</b></il>
                    </ul>
            `

    startBtn.addEventListener('click', ()=>{
       window.location.href = url + pk
    })
        })
    );
});