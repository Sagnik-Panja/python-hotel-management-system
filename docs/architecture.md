## Architecture Diagram

![Architecture Diagram](architecture-diagram.png)

# System Architecture

The system is a modular CLI Property Management System.

Components:

- Customer Module → CRUD operations
- Room Module → inventory + billing
- Food Module → menu + billing
- Laundry Module → service billing
- Billing Engine → aggregates charges
- Database Layer → MySQL persistence

The application follows a layered architecture:

UI Layer → Service Layer → Database Layer
