## Description
This is a (highly unfinished) project where I attempt to create an agentic AI email handler that respects your data.
All data is stored locally except your UUID
Internet connection is only required to fetch this app's own data, and to send or draft the emails (unavoidably requires network access).

## Current features
None yet, I'm working on building the foundation

## Planned features
- Support for local LLM runners (e.g. Ollama) in addition to mass-market LLMs like GPT or Claude
- Support for secure mail services (in addition to the mass-market ones like Gmail and Outlook)
- Ability to read through restricted desktop files (permissions granted on whitelist basis)
- High degree of configuration

## Current end-goal
- Working desktop (MacOS & Linux) app with all planned features & relatively simple setup

## Structure
This project is split into multiple folders:
- app: This stores only main.py, the primary "run" script.
- auth: This stores the user's authentication tokens. It will remain empty on the repository.
- classes: This stores basic classes (basic interfaces for an email, email provider, LLM provider)
- config: This stores all configuration
- email_providers: This stores all currently supported or planned email providers
- install: This contains the scripts for first installation. As part of the installation, they are run once then discarded
- LLM_providers: This stores all currently supported or planned LLM providers
- UI: This stores all the code for the UI