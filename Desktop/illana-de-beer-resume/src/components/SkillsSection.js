export default function SkillsSection({ skills }) {
  return (
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
  );
}
