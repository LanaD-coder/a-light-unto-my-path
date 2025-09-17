import React from "react";

export default function ProfileSection() {
  return (
    <section
      id="profile"
      className="bg-light text-center py-5 d-flex align-items-center"
      style={{
        minHeight: "100vh",
        paddingTop: "100px",
        background: "linear-gradient(to right, #f8f9fa, #e9ecef)",
      }}
    >
      <div className="container">
        <div className="row align-items-center">
          <div className="col-md-6 mb-4 mb-md-0">
            <img
              src="/assets/images/profile-bg.png"
              alt="Profile"
              className="img-fluid rounded shadow-lg"
              style={{
                width: "80%", // fill the column
                height: "auto", // maintain aspect ratio
                maxHeight: "70vh", // scale up to 80% of viewport height
              }}
            />
          </div>
          <div className="col-md-6 text-start">
            <h1 className="display-4">
              <strong>Illana De Beer</strong>, <br></br> get to know me...
            </h1>
            <p className="lead">
              Recently I read a book by Jeffrey Fischer,{" "}
              <em>The Next Conversation: Argue Less, Learn More.</em> <br></br>{" "}
              In it, he encourages people to reflect on their personal
              values—three guiding principles that shape who you are. <br></br>
              <br></br> His was inspiring:<br></br>
              1. Where there is room for kindness, I will use it. <br></br> 2.
              Tell them who I am without saying a word.<br></br> 3. If I can’t
              be a bridge, I’ll be a lighthouse.<br></br>
              <br></br>You might think, “What an unusual way to start a resume.”
              But as a 44-year-old who has lived in Asia, Europe, Great Britain,
              and Africa, and worked across a variety of industries, I’ve come
              to realize that a job is more than just skills—it’s about how you
              fit within a company’s culture. Skills can always be learnt, but
              values and personality define how we connect with others. That’s
              why I created this site: to share not just my projects, but also a
              glimpse of who I am. These projects are my first steps into
              full-stack program development. They reflect both my learning
              journey and my personality—things I’m passionate about, designed
              in my own style. Alongside coding, I bring experience in logistics
              and graphic design, giving me a unique perspective that blends
              structure with creativity. <br></br>
              <br></br>I hope you enjoy exploring my work as much as I enjoyed
              creating it.
            </p>
            <a href="#projects" className="btn btn-primary btn-lg mt-3">
              See My Work
            </a>
          </div>
        </div>
      </div>
    </section>
  );
}
