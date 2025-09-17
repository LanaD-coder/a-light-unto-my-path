import React from "react";

export default function MilestonesSection({ milestones }) {
  return (
    <section id="milestones" className="container py-5">
      <h2 className="mb-4">Milestones</h2>
      <div className="row g-4">
        {milestones.map((milestone, index) => (
          <div key={index} className="col-md-4">
            <div className="card h-100 shadow-sm text-center p-3">
              <h5 className="card-title">{milestone.title}</h5>
              <span className="badge bg-info mb-3">{milestone.type}</span>
              <a
                href={milestone.file}
                target="_blank"
                rel="noopener noreferrer"
                className="btn btn-primary"
              >
                View Document
              </a>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
