# AutoSys Workload Automation

AutoSys Workload Automation (formerly CA AutoSys, now Broadcom AutoSys) is an enterprise-level job scheduling and workload automation platform that manages and automates the execution of batch jobs, scripts, and business processes across heterogeneous IT environments.

## Objects

- Machines: 
  - Real Machine
  - Virtual Machine
  - availbale on network accessible to AutoSys
  - AutoSys-supported agent is intalled. 
- Jobs: tasks that are automated. e.g., execute script, run command, start program and execute cloud service.
  - Attributes hold every info about the job and specify the job properties.
  - Supports 60 + job types.
  - captures exit code  and run status

## Job Types
AutoSys supports various types of jobs, including:
- **Command Jobs (c)**: Executes a single command or script on a specified machine.
- **Box Jobs (b)**: Container for organizing other jobs; controls their execution as a group.
- **File Trigger**: Triggers job execution when a file is created, updated, deleted, expanded, or shrunk, or when a file exists or doent not exists. 
- **File Watch Jobs (f)**: Waits for a file to arrive or change before executing using `watch_file` attributes.

## Job Creation Methods:

- JIL
- Web UI
- Rest API

### JIL (Job Information Language)
JIL is AutoSys's domain-specific language used to define and manage objects such as jobs, machines, external instances and resoucrces.

### Key JIL Attributes:
- **Basic Properties**: `job_type`, `machine`, `owner`, `permission`
- **Scheduling**: `days_of_week`, `start_times`, `run_calendar`
- **Dependencies**: `condition`, `success_codes`, `failure_codes`
- **File Watching**: `watch_file`, `watch_file_min_size`
- **Resources**: `resources`, `priority`, `max_run_alarm`


## Job Dependencies and Conditions
Jobs can be dependent on other jobs using condition statements:
- **Success Conditions**: `condition: success(job_name)` - triggers when specified job completes successfully.
- **Failure Conditions**: `condition: failure(job_name)` - triggers when specified job fails.
- **Termination Conditions**: `condition: terminated(job_name)` - triggers regardless of job outcome.
- **Done Conditions**: `condition: done(job_name)` - triggers when job reaches any final state.
- **Complex Conditions**: Multiple conditions can be combined using AND (&) and OR (|) operators.

## Job Scheduling
Job scheduling can be based on:
- **Date and Time**: Fixed intervals using `days_of_week`, `start_times`, `run_calendar`.
- **Cron-Like Expressions**: Not native to AutoSys, but similar functionality through date/time combinations.
- **Calendar-Based Schedules**: Business calendars for holidays, weekends, fiscal periods using `run_calendar` and `exclude_calendar`.
- **Repeated Intervals**: Jobs that repeat using `run_window` and time-based conditions.
- **Event-Driven**: Jobs triggered by file arrival, job completion, or external events.

## Managing Jobs with Resources (Virtual Resources)
Resources in AutoSys are used to:
- **Limit Concurrent Executions**: Prevent resource contention using `max_run_alarm`.
- **Control Resource Access**: Define resource pools that jobs must acquire before running.
- **Manage Load Balancing**: Distribute jobs across available machines.
- **Coordinate Shared Resources**: Ensure exclusive access to databases, files, or systems.
- **Implement Throttling**: Control the number of jobs running simultaneously.

## Event-Based and Conditional Scheduling
AutoSys uses condition-based scheduling rather than simple event triggers:

### Common Condition Patterns:
- **Job Success Dependencies**: `condition: success(daily_extract)`
- **Job Failure Handling**: `condition: failure(data_load)`
- **File-Based Triggers**: File watcher jobs with `watch_file: /path/to/file`
- **Time Windows**: `condition: success(job_a) & time(08:00)`
- **Complex Logic**: `condition: (success(job1) | success(job2)) & done(job3)`

### Job States and Control:
- **ON_HOLD**: Manually suspend job execution
- **ON_ICE**: Temporarily disable job from scheduling
- **INACTIVE**: Job definition exists but won't be scheduled
- **RUNNING**: Job is currently executing
- **SUCCESS/FAILURE**: Final completion states

