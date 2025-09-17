// src/components/Navbar.js
import React from "react";

export default function Navbar({ onContactClick }) {
  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-light fixed-top shadow-sm">
      <div className="container">
        <a className="navbar-brand" href="#profile">
          <img
            src="/assets/images/logo.png"
            alt="Logo"
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
              <a className="nav-link" href="#profile">
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
                <li>
                  <a className="dropdown-item" href="#education">
                    Education
                  </a>
                </li>
              </ul>
            </li>
            <li className="nav-item">
              <button
                className="btn btn-link nav-link"
                onClick={onContactClick}
              >
                Contact
              </button>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
}
