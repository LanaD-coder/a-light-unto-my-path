export default function ProjectsSection({ projects }) {
  return (
    <section id="projects" className="container py-5">
      <h2 className="mb-4 text-center">Projects</h2>
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
                {project.grade && (
                  <span className={`badge bg-${project.badgeColor} mt-2`}>
                    Grade: {project.grade}
                  </span>
                )}
              </div>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
