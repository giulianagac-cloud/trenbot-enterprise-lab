# Shared Contracts

This folder contains lightweight shared contract definitions for the chat API.

- [chat.py](/home/giuli/trenbot-enterprise/shared/contracts/chat.py) documents the Python-side contract model.
- [chat.ts](/home/giuli/trenbot-enterprise/shared/contracts/chat.ts) documents the TypeScript-side contract model.

The backend and frontend currently each own their runtime models, but these files establish a clear place for future contract synchronization and versioning.

