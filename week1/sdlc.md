# Software

- What is software?
## Characteristics of Software

1. Software is developed or engineered. It is not manufactured.
2. Software doesn’t “wear out”. It "deteriorates!"
3. Although the industry is moving toward component-based construction, most
software continues to be custom built.

# Software application domains

1. System software
2. Application software
3. Engineering/scientific software
4. Embedded software
5. Product-line software
6. Web application
7. Artificial intelligence software
8. Legacy Software

# Software engineering

- What is software engineering?

To build software that meets all the challenges of the 21st century, few realities sould be considered:

- A concerted effort should be made to understand the problem before a software solution is developed.
- Design becomes a pivotal activity.
- Software should exhibit high quality.
- software should be maintainable

<b>Conclusion:</b> Software in all of its forms and across all
of its application domains should be engineered.

<b>Software Engineering:</b>  The application of a systematic, disciplined, quantifiable approach
to the development, operation, and maintenance of software; that is, the application of
engineering to software.

Questions:

- Why does it take so long to get software finished?
- Why are development costs so high?
- Why can’t we find all errors before we give the software to our customers?
- Why do we spend so much time and effort maintaining existing
programs?
- Why do we continue to have difficulty in measuring progress as software is
being developed and maintained?

<i>"It can be done fast, it can be done right, it can be done cheap. you can choose only two"</i>

# SDLC

Software development lifecycle describes the phases of software developmnet and the order in which the phases are executed.

1.  Requirement gathering and Analysis
2. Planning
4. Design
5. Implementation
6. Testing
7. Deployment
8. Maintainance

# Waterfall Model

Waterfall model is a linear or sequential model for project management. It works on fixed dates, requiremnts and outcomes.



A typical Waterfall project is chronological and is made up of the following phases:

1. Requirements

Written requirements for all stages is put into a single document and used for verification of each stage. The document is composed of constraints and functional and non-functional needs of the project, cost, assumptions, risks, dependencies, success metrics, and timelines for completion.

2. Design

A high-level design (HLD) is created to describe the purpose, the scope of the project, the general traffic flow of each component, and the integration points (the topology). A deatiled design is created, which allows subject matter experts (SMEs) to implement the HLD design to precise details.

1. Implementation

Implementation teams work to the design to create, code, implement, and test the solution. 

4. Verification

Acceptance tests are deployed to verify that project satisfies all the initial requiremnts. If it does not, a review is done to determine any ratification actions.


5. Maintenance

After deployment if the defects are raised or new versions of products are needed they are handeled in maitainance phase.



In the Waterfall Model, each stage can only continue when each of the previous stages are completed and signed off.


**Benifits:**

- cost and timeline can be determined in the begining as the project scope is static.
- The cost to fix or alter designs is minimun.
- SME's can effecticely plan their time this leads to a structured approach, that ensures that everyone understands what needs to be done and when.
- Less meetings and independent work enviorment.
- Detailed documentation and design will create some flexibility to add or remove existing key members in the team.

**Drawbacks:**

- New changes are hard to incorporate.
- Relatively slow pace and not suitable for rapid releases.
- HArd to estimate the exact time as any new change will lead to repetition of process.

# Agile

Agile methodology Agile methodology promotes iterative development with incremental releases.  It is iterative because it plans for the work of one iteration to be improved upon in subsequent iterations. It is incremental because completed work is delivered throughout the project.

![Agile](images/Agile.PNG)

The values and principles of the ‘Manifesto for Agile Software Development’ are:

**Values**
- Individuals and interactions over processes and tools
- Working software over comprehensive documentation
- Customer collaboration over contract negotiation
- Responding to change over following a  plan


**Principles**

- Customer satisfaction through early and continuous software delivery
- Accommodate changing requirements throughout the development process
- Frequent delivery of working software
- Collaboration between the business stakeholders and developers throughout the project
- Support, trust, and motivate the people involved
- Enable face-to-face interactions
- Working software is the primary measure of progress
- Agile processes to support a consistent development pace
- Attention to technical detail and design enhances agility
- Simplicity
- Self-organizing teams encourage great architectures, requirements, and designs
- Regular reflections on how to become more effective

![Agile vs Waterfall](images/AgilevsWaterfall.PNG)


The work and requirents are classified as:

Let's define each of these terms in the context of software development:

1. **Feature:** A feature refers to a distinct piece of functionality or behavior in a software product that provides value to its users or customers. It represents a specific capability that the software offers.

2. **Enhancement:** An enhancement refers to an improvement or addition to an existing feature or functionality in a software product. It aims to enhance the user experience, performance, or functionality of the system beyond its current state.

3. **Bug:** A bug, also known as a defect or issue, refers to an error, flaw, or unintended behavior in a software product. Bugs can cause the software to behave incorrectly, produce unexpected results, or crash. Bug fixing involves identifying, investigating, and resolving these issues to ensure the software functions as intended.

4. **Epic:** An epic represents a large body of work that cannot be completed within a single iteration or sprint. It represents a significant feature or functionality that provides business value. Epics are usually too big to estimate in terms of time or effort accurately. They are often broken down into smaller, manageable user stories or tasks.

5. **User Story:** A user story is a concise, written description of a feature or functionality from the perspective of a user or customer. It captures the "who," "what," and "why" of a requirement in a simple format. User stories are smaller than epics and can be estimated and completed within a single iteration. They serve as a means of communication and collaboration between stakeholders and the development team. The user stories are formated as As a "role"(who), I want to "Action"(what) so that benifit(why).

6. Task: A task represents the smallest unit of work required to complete a user story or an epic. It breaks down the work into specific actions or steps that need to be taken to implement a user story. Tasks are even more granular than user stories and can be estimated and completed within a short timeframe, typically a few hours to a day.

In summary, a feature represents a distinct functionality, an enhancement improves an existing feature, a bug refers to an error or flaw, an epic represents a large feature or functionality, a user story captures a requirement from a user's perspective, and a task represents a small unit of work required to complete a user story or an epic. These terms are commonly used in agile software development to plan, prioritize, and implement software projects.

Most commonly used agile methodolgies are:

### 1. Scrum Methodology

![Scrum](images/Scrum.PNG)

Scrum is an agile software development  method with principiles that are consistent with agile manifesto. The process contains the framwork activities: requiremnt, analysis, design, evolution and delivery. Within each framework activity a process pattern is implemented it is called as sprint.

- Work in sprint will vary depending on the problem in hand and cna ve modified in real time by the scrum team.

**Product Backlog:** The Product Backlog is a prioritized list of all the desired features, enhancements, and bug fixes for the software product. It represents the overall scope of work that needs to be completed. The Product Owner is responsible for maintaining and prioritizing the backlog based on business value and stakeholder input.

**Sprint Backlog:** The selected items from the Product Backlog are moved to the Sprint Backlog. The Sprint Backlog is a subset of the Product Backlog and contains the user stories or tasks that the development team commits to completing during the sprint. The team decomposes user stories into smaller tasks and estimates the effort required for each task.

**Scrum team roles:**

1. Product owner: Product expert who represents the stakeholders, and is the voice of the customer.
2. Development team: Group of professionals who deliver the product (developers, programmers, designers).
3. Scrum master: Organized servant-leader who ensures the understanding and execution of Scrum is followed.

**Scrum events:**

1. **Sprint:** Iterative time boxes where a goal is accomplished. Time frame does not exceed one calendar month and are consistent throughout the development process.
2. **Sprint planning:** The entire Scrum team get together at the beginning of every Sprint to plan the upcoming sprint.
3. **Daily Scrum:** Usually a 15 minute meeting held at the same time, every day of the Sprint, where the following questions are answred:

- What did you do since last Scrum meeting?
- Do you have any Obstacles?
- What will you do before next meeting?

4. **Sprint Execution:** The development team works on the tasks assigned to them in the Sprint Backlog. They collaborate, code, test, and integrate the features incrementally. The team has the autonomy to decide how to complete the work, but they collaborate closely to ensure a cohesive and integrated product.
   
5. **Sprint review:** An informal meeting held at the end of every Sprint where the Scrum team present their Increment to the stakeholders, and discuss feedback.
6. **Sprint retrospective:** A meeting where the Scrum team reflect on the proceedings of the previous Sprint and establish improvements for the next Sprint.


#### Story ponting

Story pointing is a technique used in agile development to estimate the relative effort or complexity of user stories. It helps the development team understand the effort required to implement a user story compared to others. The most common scale used for story pointing is the Fibonacci sequence (e.g., 1, 2, 3, 5, 8, 13). Each number represents a story point, which is an arbitrary unit of effort. The team collectively assigns story points to each user story based on complexity, technical challenges, and other factors.

It's important to note that story points and effort estimation are not precise measurements but rather a tool for the team to facilitate discussions and make informed decisions during the development process.


**Reference:**

1. <i>Software Engineering: A Practitioner's Approach</i>

