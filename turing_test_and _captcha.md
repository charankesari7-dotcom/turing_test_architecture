# I. Turing Test Implementation Architecture

The Turing Test is a test to see if a machine can talk like a human.

## Architecture Components

### 1. User Interface

This is where a human judge chats with two people:

* A real human

* A computer program (AI)

The judge does not know who is human and who is the AI.

### 2. Conversation Manager

It helps messages go back and forth between:

* The judge

* The AI

* The human

### 3. AI Response Generator

The AI answers the judges questions using:

* A way to understand language (Natural Language Processing)

* A database of facts (knowledge base)

* A model of how to have a conversation (dialogue model)

### 4. Human Participant Module

Another human answers the questions on their own.

### 5. Evaluation Module

After chatting for a bit the judge decides who is human.

If the judge can't tell the AI from a human the system passes the Turing Test.

## Turing Test System Architecture

<img width="308" height="186" alt="image" src="https://github.com/user-attachments/assets/21b9eba0-d17a-4874-8c29-1d536bb7d72f" />

# II. CAPTCHA Implementation Architecture

CAPTCHA systems help tell humans and computers

For my idea from assignment 1 it's a Common-Sense CAPTCHA that needs real-world knowledge.

## Example Question

How do you make tea?

* Boil water

* Pour into cup

* Add a tea bag

* Drink

A human knows the order. Computers struggle because they don't understand cause and effect.

## CAPTCHA System Components

### 1. Challenge Generator

It creates challenges for CAPTCHA.

Types:

* Image recognition

* Text distortion

* Real-world sequence problems (my idea)

## Example Challenge

Put these steps in order:

* [ bread, in toaster]

* [Eat toast]

* [Turn on toaster]

* [Take toast out]

### 2. Knowledge Database

It stores task sequences that people know.

Example:

Task: Brushing teeth

1. Apply toothpaste

2. Brush teeth

3. Rinse mouth

### 3. Challenge Presenter

It shows the CAPTCHA to the user.

Example formats:

* Drag and drop ordering

* Multiple choice ordering

* Image sequence arrangement

### 4. Verification Engine

It checks the users answer against the sequence.

If the users answer matches the sequence then...

### 5. Bot Detection Layer

It looks for patterns like:

* Fast answers

* Repeated attempts

* Strange interactions

## CAPTCHA Architecture Diagram

User --> Challenge Interface --> Challenge Generator --> Knowledge Database-->Verification Engine --> Human or Computer Decision
