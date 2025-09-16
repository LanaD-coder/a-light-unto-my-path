import { useState } from "react";
import { Modal, Button } from "react-bootstrap";
import { FaExclamationCircle, FaLightbulb, FaPhone } from "react-icons/fa";

export default function App() {
  const [showModal, setShowModal] = useState(false);

  const handleClose = () => setShowModal(false);
  const handleShow = () => setShowModal(true);

  const projects = [
    {
      title: "Unleash",
      description: "Brief description of project one.",
      image: "/assets/images/Screenshot-mockup.png",
      grade: "Merit",
      badgeColor: "success",
    },
    {
      title: "Oh no Lola",
      description: "Brief description of project two.",
      image: "/assets/images/mockup-hp.png",
      grade: "Pass",
      badgeColor: "warning",
    },
    {
      title: "Salon La Vida",
      description: "Brief description of project three.",
      image: "/assets/images/mockup.png",
      link: "https://salon-lavida-service-app-30430987c2a8.herokuapp.com/",
      grade: "Merit",
      badgeColor: "success",
    },
    {
      title: "A light unto my path",
      description: "Brief description of project four.",
      image: "/assets/images/hp-mockup.png",
      link: "https://www.alightuntomypath.de/",
      grade: "Merit",
      badgeColor: "success",
    },
    {
      title: "Print & Design",
      description: "Brief description of project five.",
      image: "/assets/images/homepage.png",
      link: "https://print-design-d837920c6712.herokuapp.com/",
      grade: "Pass",
      badgeColor: "warning",
    },
    {
      title: "Calli Der Camper rental",
      description: "Brief description of project six.",
      image: "/assets/images/jarental.png",
      link: "https://www.callidercamper.de",
    },
  ];

  const skills = [
    {
      title: "HTML",
      image: "/assets/images/html-1.svg",
    },
    {
      title: "CSS",
      image: "/assets/images/css-3.svg",
    },
    {
      title: "JavaScript",
      image: "/assets/images/javascript-r.svg",
    },
    {
      title: "React",
      image: "/assets/images/react-2.svg",
    },
    {
      title: "Python",
      image: "/assets/images/python-5.svg",
    },
    {
      title: "Adobe InDesign",
      image: "/assets/images/adobe-indesign-cc-icon.svg",
    },
    {
      title: "Adobe Photoshop",
      image: "/assets/images/adobe-photoshop-2.svg",
    },
    {
      title: "Adobe Illustrator",
      image: "/assets/images/adobe-illustrator-cc-3.svg",
    },
  ];

  const designs = [
    {
      title: "Birthday Memory book Layout",
      description: "Creative 50 page book designed in Adobe InDesign.",
      images: ["/assets/images/ria-bday.png", "/assets/images/book.png"],
      tool: "Adobe InDesign, Illustrator and Photoshop",
    },
    {
      title: "Fasting Group Logo",
      description: "Hand-drawn logo for a fasting group.",
      image: "/assets/images/sos.png",
      tool: "Adobe Photoshop and Illustrator",
    },
    {
      title: "Vector signage design",
      description: "Vectorised image generation for metal CNC cutting",
      image: "/assets/images/3diere.png",
      tool: "Adobe Illustrator",
    },
    {
      title: "Guesthouse flyer design",
      description: "Mockup design for eco-friendly guesthouse flyer.",
      image: "/assets/images/lavender-dreams-flyer.jpg",
      tool: "Adobe Illustrator",
    },

    {
      title: "Care home Flyer series",
      description: "A series of flyers addressing all services provided",
      images: [
        "/assets/images/nitacare.png",
        "/assets/images/nitacare-piliativ.png",
      ],
      tool: "Adobe Photoshop",
    },
  ];

  const education = [
    {
      school: "Kaplan College, Singapore",
      qualification: "Diploma in Shipping and Logistics Management",
      period: "2010 - 2011",
    },
    {
      school: "Code Institute",
      qualification: "Diploma in Full Stack Software Development",
      period: "Dec. 2024 - May 2025",
    },
    {
      school: "Udemy",
      qualification: "Adobe Masterclass Certificate",
      period: "2023",
    },
  ];

  const documents = [
    {
      title: "Diploma in Shipping & Logistics Management",
      file: "/assets/docs/kaplan-certificate.pdf",
      type: "Certificate",
    },
    {
      title: "Diploma in Full Stack Software Development",
      file: "/assets/docs/ci_diploma.pdf",
      type: "Certificate",
    },
    {
      title: "Adobe Masterclass Certificate",
      file: "/assets/docs/udemy-Adobe-masterclass.jpg",
      type: "Certificate",
    },
    {
      title: "Reference Letter - GLOBUS Markthalle Essen",
      file: "/assets/docs/globus-arbeitszeugnis.pdf",
      type: "Reference Letter",
    },
  ];

  return (
    <div>
      {/* Navbar */}
      <nav className="navbar navbar-expand-lg navbar-light bg-light fixed-top shadow-sm">
        <div className="container">
          <a className="navbar-brand" href="#home">
            <img
              src="/assets/images/logo.png"
              alt="My Logo"
              height="40"
              className="d-inline-block align-text-top"
            />
          </a>
          <button
            className="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNav"
            aria-controls="navbarNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav ms-auto">
              <li className="nav-item">
                <a className="nav-link" href="#home">
                  Home
                </a>
              </li>
              <li className="nav-item dropdown">
                <a
                  className="nav-link dropdown-toggle"
                  href="#profile"
                  id="profileDropdown"
                  role="button"
                  data-bs-toggle="dropdown"
                  aria-expanded="false"
                >
                  Profile
                </a>
                <ul className="dropdown-menu" aria-labelledby="profileDropdown">
                  <li>
                    <a className="dropdown-item" href="#projects">
                      Projects
                    </a>
                  </li>
                  <li>
                    <a className="dropdown-item" href="#design">
                      Graphic Design
                    </a>
                  </li>
                  <li>
                    <a className="dropdown-item" href="#skills">
                      Skills
                    </a>
                  </li>
                </ul>
              </li>
              <li className="nav-item">
                <button className="btn btn-link nav-link" onClick={handleShow}>
                  Contact
                </button>
              </li>
            </ul>
          </div>
        </div>
      </nav>

      {/* Sections */}
      <section id="home" className="bg-light text-center">
        <div className="container">
          <img
            src="/assets/images/profile-bg.png"
            alt="My Profile Picture"
            className="mb-3 shadow-sm"
            width="500"
            height="600"
          />
          <h1 className="display-4">Illana De Beer, get to know me...</h1>
          <p className="lead">
            Recently I read a book by Jeffrey Fischer,{" "}
            <em>The Next Conversation: Argue Less, Learn More.</em> <br></br> In
            it, he encourages people to reflect on their personal values—three
            guiding principles that shape who you are. <br></br>
            <br></br> His was inspiring:<br></br>
            1. Where there is room for kindness, I will use it. <br></br> 2.
            Tell them who I am without saying a word.<br></br> 3. If I can’t be
            a bridge, I’ll be a lighthouse.<br></br>
            <br></br>You might think, “What an unusual way to start a resume.”
            But as a 44-year-old who has lived in Asia, Europe, Great Britain,
            and Africa, and worked across a variety of industries, I’ve come to
            realize that a job is more than just skills—it’s about how you fit
            within a company’s culture. Skills can always be learnt, but values
            and personality define how we connect with others. That’s why I
            created this site: to share not just my projects, but also a glimpse
            of who I am. These projects are my first steps into full-stack
            program development. They reflect both my learning journey and my
            personality—things I’m passionate about, designed in my own style.
            Alongside coding, I bring experience in logistics and graphic
            design, giving me a unique perspective that blends structure with
            creativity. <br></br>
            <br></br>I hope you enjoy exploring my work as much as I enjoyed
            creating it.
          </p>
        </div>
      </section>

      <section id="education" className="container py-5">
        <h2 className="mb-4">Education</h2>
        <div className="list-group">
          {education.map((edu, index) => (
            <div key={index} className="list-group-item shadow-sm mb-2">
              <h5>{edu.qualification}</h5>
              <p className="mb-1">{edu.school}</p>
              <small className="text-muted">{edu.period}</small>
            </div>
          ))}
        </div>
      </section>

      <section id="documents" className="bg-light py-5">
        <div className="container">
          <h2 className="mb-4">Documents</h2>
          <div className="row g-4">
            {documents.map((doc, index) => (
              <div className="col-md-4" key={index}>
                <div className="card h-100 shadow-sm text-center p-3">
                  <div className="card-body">
                    <h5 className="card-title">{doc.title}</h5>
                    <span className="badge bg-info mb-3">{doc.type}</span>
                    <a
                      href={doc.file}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="btn btn-primary"
                    >
                      View Document
                    </a>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section id="projects" className="container py-5">
        <h2 className="mb-4">Projects</h2>
        <div className="row g-4">
          {projects.map((project, index) => (
            <div className="col-md-4" key={index}>
              <div className="card h-100 shadow-sm">
                <img
                  src={project.image}
                  className="card-img-top"
                  alt={project.title}
                />
                <div className="card-body d-flex flex-column">
                  <h5 className="card-title">{project.title}</h5>
                  <p className="card-text flex-grow-1">{project.description}</p>

                  {/* Render Visit Website only if link exists */}
                  {project.link && (
                    <a
                      href={project.link}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="btn btn-primary mt-2"
                    >
                      Visit Website
                    </a>
                  )}

                  <span className={`badge bg-${project.badgeColor} mt-2`}>
                    Grade: {project.grade}
                  </span>
                </div>
              </div>
            </div>
          ))}
        </div>
      </section>

      <section id="design" className="container py-5">
        <h2 className="mb-4">Graphic Design</h2>
        <div className="row g-4">
          {designs.map((design, index) => (
            <div className="col-md-6" key={index}>
              <div className="card h-100 shadow-sm">
                <div className="card-body">
                  <h5 className="card-title">{design.title}</h5>
                  <p className="card-text">{design.description}</p>
                  <span className="badge bg-info mb-3">
                    Tool: {design.tool}
                  </span>

                  {/* Render single or multiple images */}
                  {design.images
                    ? design.images.map((img, i) => (
                        <img
                          key={i}
                          src={img}
                          alt={`${design.title} - ${i + 1}`}
                          className="img-fluid mb-2"
                        />
                      ))
                    : design.image && (
                        <img
                          src={design.image}
                          alt={design.title}
                          className="img-fluid mb-2"
                        />
                      )}
                </div>
              </div>
            </div>
          ))}
        </div>
      </section>

      <section id="skills" className="bg-light py-5">
        <div className="container">
          <h2 className="mb-4">Skills</h2>
          <div className="row g-4">
            {skills.map((skill, index) => (
              <div className="col-6 col-md-3" key={index}>
                <div className="card h-100 text-center shadow-sm p-3">
                  <img
                    src={skill.image}
                    className="card-img-top mx-auto"
                    alt={skill.title}
                    style={{
                      width: "60px",
                      height: "60px",
                      objectFit: "contain",
                    }}
                  />
                  <div className="card-body">
                    <h6 className="card-title">{skill.title}</h6>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-light text-center py-3">
        <p>&copy; 2025 MyProfile. All Rights Reserved.</p>
      </footer>

      {/* Contact Modal */}
      <Modal show={showModal} onHide={handleClose} centered>
        <Modal.Header closeButton>
          <Modal.Title>Contact Me</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <p>
            <strong>Email:</strong> c.wnt.nd1053@gmail.com
          </p>
          <p>
            <FaPhone style={{ color: "green", marginRight: "5px" }} />
            <strong>Phone:</strong> +49 152 1025 7226
          </p>
          <form>
            <div className="mb-3">
              <label htmlFor="message" className="form-label">
                For easy contact, please send me a message!
              </label>
              <textarea
                id="message"
                className="form-control"
                rows="3"
                placeholder="Type your message here..."
              ></textarea>
            </div>
          </form>
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleClose}>
            Close
          </Button>
          <Button variant="primary">Send Message</Button>
        </Modal.Footer>
      </Modal>
    </div>
  );
}
