# Milestone 1 - Dashboard proposal

In this milestone,
you will set-up your project for development and submit a dashboard proposal.

## Project background

DSCI 532 is a project-based course where you will be working in a team of 3-4 students
with the goal of designing a dashboard
for interactive data visualization, exploration, and communication.
In addition to principles of effective dashboard development,
this project will allow you to practice concept design,
desining for a specific target audience,
and practice the teamworking skills you learned in previous courses.

As a team, you will create a scenario for your dashboard,
which includes choosing the target audience (internal research team, public communication, etc),
who you are (part of a company, NGO, research team, student group, etc),
and the goal of building the app for your target audience
(communicating your research to the public, deriving market insight, driving end user decision making, etc).
It is fine if this changes slightly as your are building the app,
but try to stick to it as much as possible
so that you have a clear direction throughout.

Another group will take on the hat of your intended target audience,
try using your app,
and give you feedback on their experience.
You will then incorporate this feedback into one last round of improvements
to finalize your data product.
The projects will be developed in public repos on GitHub.com to facilitate deployment
and so that you can share your work as part of your data science portfolio.

This process will be spread out over four milestones:

1. Pick a scenario, dataset, and target audience. Write the teamworking contract and sketch the dashboard.
2. Create and deploy a dashboard prototype.
3. Keep refining the dashboard. Give feedback on another group's M2.
4. Implement the feedback from M3 and make final improvements to the dashboard to be production ready.
   Write about what you would have improved further if you had more time.

## 1. Submission instructions and repo creation
rubric={mechanics:5}

- [Follow the general lab instructions](https://ubc-mds.github.io/resources_pages/general_lab_instructions/).
- [Click here to view a description of the rubrics used to grade the questions](https://github.com/UBC-MDS/public/tree/master/rubric).
- Create one Github repository per group under the [UBC-MDS](https://github.com/UBC-MDS) organization.
    - **Your repo has to follow the naming convention**: `DSCI-532_2024_grpnum_appname`,
      where `grpnum` is your group number and `appname` is the name that you have chosen for your app/dashboard,
      e.g. `DSCI-532_2024_3_healthcare-tracker`.
- For every milestone, **you must [create a release on GitHub.com](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository#creating-a-release) before the submission deadline**.
    - We will grade all files in the repo at the state they were in when you created the release.
      This means that you can continue to make changes in the repo
      without worrying about messing up your grading for the previous milestone.
    - Expectations for the relases:
        - Increment the minor version number for each milestone.
          So for M1, the release should be named `0.1.0`, for M2, `0.2.0`, and so on
          (you're free to make patch releases in between milestones if you want to practice,
          e.g., `0.1.1`, `0.1.2`, etc).
        - Each release should include release notes.
          Write these directly in the release notes box on GitHub.
          At a minimum,
          the release notes should include the title of the merged PRs since the last milestone,
          and indicate which of these fixed existing bug
          and which added new features.
- You need to **submit two files on gradescope:**
  - `link-to-release.ipynb`: Includes a single markdown cell with the link to your M1 release on GitHub.
  - `teamwork-contract.md`: Your teamwork contract as per the instructions in the section [Teamwork contract](#3-teamwork-contract)
    (do not include this file in your GitHub repo as it might contain private information).

## 2. Expectations for working collaboratively on GitHub
rubric={accuracy:10}

For the duration of this project,
you're expected to work with a Github flow workflow,
and follow the guidelines outlined in [the DSCI 524 lecture material](https://pages.github.ubc.ca/MDS-2023-24/DSCI_524_collab-sw-dev_students/release/milestone1/milestone1.html#expectations).
In addition,
you are also expected to adhere to (i.e. will be graded on) the following in 532:

- Always work on feature branches, not directly on main.
- Commit to your branch often; each commit should be atomic
  (include only one meaningful unit of changes).
    - `git add --patch` is your friend.
- Write descriptive, brief commit messages that explain the purpose of the commit.
    - Commit messages should be capitalized and complete the sentence "This commit will..."
    - Good examples: "Make the readme more welcoming", "Refactor optional import logic", "Enable PPI setting on PNG CLI export"
    - Bad examples: "added notebook", "Update analysis", "Fixes", "I hope this works", "asdfsdfasdf" (we've all been there)
- Break out the feedback from the TA's from Gradescope
  into individual issues so that you can track them in your project
  and address each pieace of feedback separately.
- Assign team members to issues and [close them via PRs using keywords](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue).
- All code that is added to the repo should come via PRs,
  no code should be pushed straight to `main`.
    - Each PR should contain one main feature/fix
    (possibly consiting of a few tightly connected smaller features/fixes).
    - Each PR should have one approving review before being merged.
    - Only use ["squash and merge"](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/about-pull-request-merges#squash-and-merge-your-commits),
    so that you can keep an easy to read commit history on `main`
    while also being able to track details for each commit via the PR link in the commit message.
        - To make this the default, you can go to `Settings` and unclick `Allow merge commits` under `Pull Requests`.

#### General Git/Github tips and reminders

- Every time you work on the project,
  you should first pull the upstream changes.
- Push your branch to the remote repo at least once a day
  even if you don't create the PR yet (so that you have an online backup).
- Don't blindly approve PRs, add comments, request changes, and do revisions before merging.
- [Read this article for how to create effecitve PRs](https://medium.com/@greenberg/writing-pull-requests-your-coworkers-might-enjoy-reading-9d0307e93da3)
- [Read this article if you want to know more about squash merging](https://blog.dnsimple.com/2019/01/two-years-of-squash-merge/).

## 3. Teamwork contract
rubric={reasoning:10}

Use [what you learned in DSCI 522](https://pages.github.ubc.ca/MDS-2023-24/DSCI_522_dsci-workflows_students/release/milestone1/milestone1.html#draft-a-team-work-contract)
to build a team work contract,
formalizing how you will work together during this project.

## 4. Repository structure
rubric={accuracy:16}

Use [what you learned in DSCI 522](https://pages.github.ubc.ca/MDS-2023-24/DSCI_522_dsci-workflows_students/release/milestone1/milestone1.html#create-an-appropriate-file-directory-structure-for-a-data-analysis-project)
to create the following files in your repo root (this will be graded using a similar rubric as for M1 in 522):

1. `README.md` (the project title and a summary of its purpose in ~3-4 sentences)
2. `LICENSE.md` (include the license for both software and non-software content)
3. `CODE_OF_CONDUCT.md` (include a citation if you used a template from elsewhere)
4. `CONTRIBUTING.md` (include a citation if you used a template from elsewhere)
5. `src/app.py` or `src/app.R` (this file can be empty for now, but indicates which language you are planning to use)
6. `data/raw/` (should inlucde your chosen raw data file(s); indicate in the proposal if you plan to load from an external source instead)
7. `notebooks/` (optional: if you start doing EDA, include your notebooks in this folder)
8. `environment.yml` (can contain just the basics for now, e.g. the libraries for the dashboard, data wrangling, and vizualization; include version numbers)
9. `reports/m1_proposal.md` (see below)
10. `img/sketch.png` (see below)

## 5. Proposal

The proposal should be written as a markdown document in your repo (`reports/m1_proposal.md`),
be **max** 1,000 words in length,
and include the following sections:

1. Motivation and purpose
2. Description of the data
3. Research questions
4. App sketch and description

You will be assessed on the reasoning underlying your proposal
as well as the quality and clarity of your writing.
Each of the proposal sections are described below and include an example of what is expected.
You don't have to write your own proposal _exactly_ the same as the examples, they just serve as inspiration.

You will not be penalized if you can't implement everything in your proposal,
or if your app changes due to technical or time limitations.
However, still try to assess whether you will be able to implement what you are proposing
in the time frame of the course
(this is admittedly hard since you have not worked with the dashboard frameworks before,
but it is good to have it in mind already in the planning phase).

### Section 1: Motivation and Purpose
rubric={reasoning:12}

In a few sentences, provide motivation for why you are creating a dashboard:

- Who is your target audience, and what role are you embodying?
- What is the problem the target audience is facing and why is it important to solve?
- How can your dashboard assist in solving this problem for the intended target audience?

The installation of a household solar energy system can be complicated for interested house owners. If we can visualize the potential savings of solar panels according to location and size according to different individuals, we can potentially motivate the house owners more for installation. 

To clearly communicate the benefits of these panels, we will use two data sets. We will use the mean daily electricity production of different locations in Canada using a standard solar panel (efficiency = 20%.) Then we will combine it with the electricity price of each province, to calculate how much monetary value of electricity each square meter of solar panel is able to generate daily. Then we will convert the value to annual saving and allow the users to choose the size of their installation. 

You can read the [Project background](#project-background) section for some rough ideas.
Be brief and clear.
Example writeup:

> Our role: Data scientist consultancy firm
>
> Target audience: Health care administrators
>
> Missed medical appointments cost the healthcare system a lot of money and affects the quality of care.
> If we could understand which factors lead to missed appointments
> it may be possible to reduce their frequency and use the saved resources to improve patient outcomes.
> To address this challenge,
> we propose building a data visualization app that allows health care administrators
> to visually explore a dataset of missed appointments to identify common factors.
> Our app will show the distribution of factors contributing to appointment show/no show
> and allow users to explore different aspects of this data
> by filtering and re-ordering on different variables
> in order to compare factors that contribute to absence.

### Section 2: Description of the data
rubric={reasoning:12}

You are allowed to select any dataset you want for this project,
as long as you have the license to use it publicly.
Finding a suitable data set can take a lot of time and effort.
You are therefore allowed to select one
that you have worked with in a previous lab/project in MDS
if you wish.

A few datasets that have been popular in previous years:

- https://www.kaggle.com/zynicide/wine-reviews/data
- https://github.com/themarshallproject/city-crime
- https://archive.ics.uci.edu/dataset/45/heart+disease

Good general resources for finding interesting datasets:

- https://github.com/fivethirtyeight/data
- https://github.com/the-pudding/data
- https://www.kaggle.com/datasets
- https://ourworldindata.org/teaching#how-can-i-use-our-world-in-data-to-teach
- https://opendata.vancouver.ca/
- https://archive.ics.uci.edu/

In your proposal,
briefly describe the dataset and the variables that you will visualize:

- Include how many rows and columns there are in the dataset (that you plan to use).
- There should be a clear link to how the dataset and the variables you describe will help you solve your target audience's problem.
- Indicate at least one new variable that you are planning to derive/engineer for your visualizations.
    - If there are no new variables to derive,
      indicate what additional information you would have liked to have in the dataset
      to better be able to answer your research questions (even if it is impossible for you to engineer it).
- If you are planning to visualize a lot of columns,
  provide a high level description of the variable types rather than listing every single column.
    - For example,
      indicate that the dataset contains a variety of categorical variables for demographics
      and provide a brief list rather than describing every single variable.
    - You may also want to consider visualizing a smaller set of variables given the short duration of this project.

To be able to include this information
you might wish to perform a brief exploratory data analysis
for you to grasp what could be interesting variables to look at in your data.
We will not be grading the EDA aspect,
but include your EDA notebooks in the public GitHub repo,
so that you have everything in one place.

Example writeup:

> We will be visualizing a dataset of approximately 300,000 missed patient appointments.
> Each appointment has 15 associated variables
> that describe the following characteristics,
> which we hypothesize could be helpful in determining why patient's miss their appointments:
>
> - Patient demographics (`patient_id`, `gender`, `age`, etc)
> - The health status of the patient (`general_health_status`, `existing_conditions` e.g. "Hypertension", "Physical disability")
> - Information about the appointment itself (`appointment_id`, `appointment_date`)
> - Whether the patient received a reminder about the appointment (`reminder_sent`)
> - Whether the patient showed up (`status`)
>
> Using this data we will also derive new variables,
> such as the time since the patient's last appointment (`days_since_last_appointment`)
> and which weekday the appointment was on (`appointment_weekday`),
> as it would be interesting to explore if these could be linked to the patient missing their appointment.

Another example of [a good description of a dataset is the Kaggle world happiness report](https://www.kaggle.com/unsdsn/world-happiness).

### Section 3: Research questions and usage scenarios
rubric={reasoning:12}

The purpose of this section is to get you to think in more detail about
how your target audience will use the app you're designing
and to account for these detailed needs in the proposal.

- For this it can be helpful to create a [brief persona description](https://engineering-shiny.org/dont-rush-into-coding.html#building-personas) of a member in your intended target audience
- Then, think about what they might want to do with your app
  and write small user story.
  User stories are typically written in a narrative style and include:
     - The specific context/background of the user
     - The overall goal of the user
     - Tasks needed to reach that goal
     - A hypothetical walkthrough of how the user would accomplish those tasks with your app
     - The outcome/action that the user would take based on the information they find in the app

An example usage scenario with tasks (tasks are indicated in square brackets)

> Mary is a policy maker with the Canadian Ministry of Health
> and she wants to understand what factors lead to missed appointments
> in order to devise an intervention that improves attendance numbers.
> She wants to be able to [explore] a dataset
> in order to [compare] the effect of different variables on absenteeism
> and [identify] the most relevant variables around
> which to frame her intervention policy.
>
> When Mary logs on to our "Missed Appointments app",
> she will see an overview of all the available variables in her dataset,
> according to the number of people that did or did not show up to their medical appointment.
> She can filter out variables for head-to-head comparisons,
> and explore which variables are most important
> in determining whether a patient will show up to their appointment.
> When she does so,
> Mary may e.g. notice that "physical disability"
> appears to be a strong predictor missing appointments,
> and in fact patients with a physical disability
> also have the largest number of missed appointments.
>
> Based on her findings from using our app,
> Mary hypothesizes that patients with a physical disability
> could be having a hard time finding transportation to their appointments,
> and decides she needs to conduct a follow-on study
> since transportation information is not captured in her current dataset.

Note that in the above example,
"physical disability" being an important variable is fictional
and serves as an example of a possible outcome/action.
For this milestone,
you don't need to conduct an analysis of your data
to figure out which variables are important and which are not.
Instead,
estimate what someone could find using your dashboard,
and how they may use this information
in a meaningful way.
If you are using a Kaggle dataset,
you may use their "Overview (inspiration)" to create your usage scenario.

### Section 4: App sketch & brief description
rubric={viz:8,reasoning:5}

Create a sketch of what you envision your app to look like.
Your sketch can be hand-drawn
or put together using a graphics editor or
slide show software.
The sketch should be saved as `img/sketch.png` and linked in this section of the proposal
so that the image shows up when reading the proposal on GitHub.

Example sketch 
(this sketch was drawn using Powerpoint
with icons from the [noun project](https://thenounproject.com/):

![Dashboard](sketch.png "App Sketch")

Complement the sketch with
a high level description of the main components in the app interface
and how the user will interact with it.
You are not required to use terminology specific to Dash/Shiny
(i.e. widgets, components, etc...).

Remember to be realistic about your expectations and plans
since you will actually be implementing this app
(but again, you will not be penalized if you need to adjust a bit in later milestones).
It is better to design a slightly more limited app
that you have time to implement well,
instead of a complicated app that you don't have time to finish.
At the same time,
you cannot just make a single bar chart and call it a day;
the app needs to have several input and output panels.
You can view the dashboards from previous years students
in the [DSCI 532 showcase](https://five32-dashboard-showcase.onrender.com)
(might take several seconds to load)
as a complexity target and to get inspiration for your final app.
Your TA will be able to help you with this as well,
and provide feedback on whether your app is too simple or too complex.

Example description:

> The app contains a landing page that shows the distribution
> (depending on data type, bar chart, density chart etc)
> of dataset factors (hypertension, physical disabilities etc.)
> colored coded according to whether patients showed up or didn't show up for an appointment.
> From a dropdown list,
> users can filter out variables from the distribution display,
> by patient demographics (i.e. only show female patients),
> by appointment data (i.e. if SMS was sent),
> and finally by the date range of appointments.
> A different dropdown menu will allow users to re-order variables
> according to the probability of patients being a no-show
> or in alphabetical order to comorbidities.
> Users can compare the distribution of co-morbidities
> by scrolling down through the app interface.


### Overall writing in the proposal
rubric={writing:5}

This heading is just to explicitly indicate that your writing in the proposal will be graded.

## 6. Start developing your app (Challenging)
rubric={reasoning:5}

It is beneficial to take the first few steps in the app development already
and push your code to GitHub.
This can be very basic,
like a general skeleton of the app code
with a few components / widgets
even if they are not yet linked together.
The important part is to
make sure everyone in the team can run the basic app on their local machine.
This will make sure you can hit the ground running
for the next milestone and don't have to deal with any setup issues.
If you are doing any EDA on the data,
please push those notebooks to the `notebooks/` directory.
You can also start planning ahead for who will do what next week
and create additional issues to capture the ideas you have for the app,
so that they don't get lost.
