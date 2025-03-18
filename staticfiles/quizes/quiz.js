$(document).ready(function () {
  const quizBox = $("#quiz-box");
  const resultsBox = $("#results-box");
  const quizForm = $("#quiz-form");
  const csrfToken = $("input[name=csrfmiddlewaretoken]").val();
  let quizId = null;

  // Handle modal button clicks and set quiz link dynamically
  $(".modal-button").click(function () {
      quizId = $(this).data("pk");
      let quizName = $(this).data("quiz");
      let numQuestions = $(this).data("questions");
      let difficulty = $(this).data("difficulty");
      let passScore = $(this).data("pass");

      // Update modal content
      $("#modal-body-confirm").html(`
          <p><strong>Quiz:</strong> ${quizName}</p>
          <p><strong>Questions:</strong> ${numQuestions}</p>
          <p><strong>Difficulty:</strong> ${difficulty}</p>
          <p><strong>Pass Score:</strong> ${passScore}</p>
      `);

      // Update the start button link to navigate to the quiz page
      $("#start-button").attr("href", `/quiz/${quizId}/start/`);
  });

  // Fetch and display quiz questions dynamically (GET request)
  if (window.location.pathname.includes("/quiz/")) {
      $.ajax({
          type: "GET",
          url: `${window.location.href}data`,
          success: function (response) {
              const data = response.data;
              quizBox.html(`<h3 class="text-center text-custom" style="color: #fbf7f4;">Quiz Questions</h3>`);

              data.forEach((element) => {
                  for (const [question, answers] of Object.entries(element)) {
                      let questionHtml = `
                          <div class="card my-3 p-3 shadow-sm">
                              <div class="mb-2">
                                  <b class="text-dark">${question}</b>
                              </div>
                      `;

                      answers.forEach((answer) => {
                          questionHtml += `
                              <div class="form-check">
                                  <input class="form-check-input ans" type="radio" id="${question}-${answer}" name="${question}" value="${answer}">
                                  <label class="form-check-label text-dark" for="${question}-${answer}">${answer}</label>
                              </div>
                          `;
                      });

                      questionHtml += `</div>`; // Close the card div
                      quizBox.append(questionHtml);
                  }
              });
          },
          error: function (error) {
              console.error("Error loading quiz data:", error);
          },
      });
  }

  // Function to handle form submission (POST request)
  function sendData() {
      const data = {};
      data["csrfmiddlewaretoken"] = csrfToken;

      $(".ans").each(function () {
          if ($(this).is(":checked")) {
              data[$(this).attr("name")] = $(this).val();
          } else {
              if (!data[$(this).attr("name")]) {
                  data[$(this).attr("name")] = null;
              }
          }
      });

      $.ajax({
          type: "POST",
          url: `${window.location.href}save/`,
          data: data,
          success: function (response) {
              console.log("Quiz results received:", response);

              // Display quiz results
              resultsBox.html(`
                  <hr>
                  <h3 class="text-center text-custom" style="color: #fbf7f4;">Quiz Results</h3>
                  <p class="text-center"><strong>Score:</strong> <span class="badge bg-primary">${response.score}</span></p>
                  <p class="text-center"><strong>Passed:</strong>
                      <span class="badge ${response.passed ? "bg-success" : "bg-danger"}">
                          ${response.passed ? "✅ Yes" : "❌ No"}
                      </span>
                  </p>
                  <h4 style="color: #fbf7f4;">Detailed Answers:</h4>
                  <ul class="list-group">
                      ${response.result.map((r) => {
                          const questionText = Object.keys(r)[0];
                          const details = r[questionText];
                          const isCorrect = details.answered === details.correct_answer;
                          return `
                              <li class="list-group-item">
                                  <b>${questionText}</b><br>
                                  <span style="color: ${isCorrect ? "green" : "red"};">
                                      Your Answer: ${details.answered || "Not Answered"}
                                  </span><br>
                                  <span>Correct Answer: <strong>${details.correct_answer}</strong></span>
                              </li>
                          `;
                      }).join("")}
                  </ul>
              `);
          },
          error: function (error) {
              console.error("Error submitting quiz:", error);
          },
      });
  }

  // Handle form submission
  quizForm.on("submit", function (e) {
      e.preventDefault();
      sendData();
  });
});
