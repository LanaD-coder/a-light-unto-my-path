import React, { useState } from "react";
import Navbar from "./components/Navbar"; // import Navbar
import ProfileSection from "./components/ProfileSection";
import EducationSection from "./components/EducationSection";
import MilestonesSection from "./components/MilestonesSection";
import ProjectsSection from "./components/ProjectsSection";
import DesignsSection from "./components/DesignsSection";
import SkillsSection from "./components/SkillsSection";
import ContactModal from "./components/ContactModal";
import { projects, skills, designs, education, milestones } from "./data";

export default function App() {
  const [showModal, setShowModal] = useState(false);

  return (
    <>
      {/* Background video */}
      <video
        autoPlay
        loop
        muted
        className="background-video"
        src="/assets/videos/67358-521707474_small.mp4"
        type="video/mp4"
      />

      {/* Navbar component */}
      <Navbar onContactClick={() => setShowModal(true)} />

      {/* Sections */}
      <div style={{ marginTop: "80px" }}>
        {" "}
        {/* top margin for fixed navbar */}
        <ProfileSection />
        <EducationSection education={education} />
        <MilestonesSection milestones={milestones} />
        <ProjectsSection projects={projects} />
        <DesignsSection designs={designs} />
        <SkillsSection skills={skills} />
      </div>

      {/* Contact modal */}
      <ContactModal show={showModal} onClose={() => setShowModal(false)} />
    </>
  );
}
