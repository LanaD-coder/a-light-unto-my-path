import React from "react";

export default function EducationSection({ education }) {
  return (
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
  );
}
