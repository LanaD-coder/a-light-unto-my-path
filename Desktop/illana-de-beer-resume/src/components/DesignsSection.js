export default function DesignsSection({ designs }) {
  return (
    <section id="design" className="container py-5">
      <h2 className="mb-4">Graphic Design</h2>
      <div className="row g-4">
        {designs.map((design, index) => (
          <div className="col-md-6" key={index}>
            <div className="card h-100 shadow-sm">
              <div className="card-body">
                <h5 className="card-title">{design.title}</h5>
                <p className="card-text">{design.description}</p>
                <span className="badge bg-info mb-3">Tool: {design.tool}</span>
                {design.images
                  ? design.images.map((img, i) => (
                      <img
                        key={i}
                        src={img}
                        alt={`${design.title} ${i}`}
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
  );
}
