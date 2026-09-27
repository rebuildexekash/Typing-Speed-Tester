# Problem Statement

Typing is something we use almost every day, whether it is for school, college, or regular work. Being able to type faster while making fewer mistakes can save time, but it is hard to know how fast and accurately you are actually typing without measuring it.
I wanted to make a simple typing speed tester that I could run directly on my computer without depending on a website. The project lets the user choose between short sentences and longer paragraphs, starts timing when they begin typing, checks their typing live, and finally shows their WPM, CPM, time taken, and accuracy.

## Objectives

- To develop a simple desktop-based typing speed tester using Python.
- To measure typing speed using WPM and CPM.
- To measure typing accuracy at both word and character level.
- To provide live feedback for correct and incorrect characters.
- To provide a simple offline application for typing practice.

## Scope

This project focuses on providing a simple desktop environment for people who are learning or practising typing. It covers basic typing practice, speed measurement, accuracy measurement, and immediate feedback while typing.
The project is limited to local typing practice and does not include online accounts, leaderboards, multiplayer features, or cloud-based storage.

## Target Users

- Kids who are learning how to type.
- Beginners who have recently started typing and want to improve their speed and accuracy.

## High-Level Features

- Sentence and paragraph mode — The user can choose what type of text they want to practice with.
- Random text selection — A different sentence or paragraph is selected for each test.
- Live typing feedback — Correct characters appear in green and incorrect characters in red while typing.
- Automatic timer — The test starts timing when the user begins typing.
- Typing statistics — The application calculates WPM, CPM, and time taken.
- Accuracy calculation — The application calculates both word accuracy and character accuracy.
- Offline desktop application — The application runs locally using Python and Tkinter without requiring an internet connection.

## Functional Requirements

### 1. Typing Mode Selection
The user can select either sentence mode or paragraph mode for the typing test.

### 2. Typing Text Selection
The program selects a typing text based on the mode chosen by the user.

### 3. Typing Test and Feedback
The program allows the user to type the selected text and provides live correct/wrong character feedback.

### 4. Performance Calculation
The program calculates the user's WPM, CPM, and time taken after the typing test.

### 5. Accuracy Calculation
The program calculates the user's word accuracy and character accuracy after the typing test.

### 6. Input Validation and Error Handling
The application checks whether the user has entered any text before submitting the typing test. If the input is empty, a warning message is displayed and the result calculation is stopped.

## Non-Functional Requirements

### 1. Usability
The application should have a simple and easy-to-use interface so that users can start a typing test without difficulty.

### 2. Performance
The application should respond quickly to user input and provide typing feedback without noticeable delay.

### 3. Reliability
The application should provide consistent results when calculating typing speed, time taken, and accuracy.

### 4. Maintainability
The program should have a clear and organized code structure so that it can be understood and modified easily.

### 5. Error Handling
The application should handle invalid or incomplete user input without crashing unexpectedly.

## System Architecture

The application follows a simple desktop application architecture.

- **User Interface:** Tkinter is used to create the window, buttons, text areas, radio buttons, and result displays.
- **Test Data:** Typing sentences and paragraphs are stored separately in `test_data.py`.
- **Typing Logic:** The main program handles text selection, typing input, timing, live feedback, and performance calculations.
- **Results:** The application displays WPM, CPM, time taken, word accuracy, and character accuracy.

## Process Flow

1. The application starts and displays the typing test interface.
2. The user selects either sentence or paragraph mode.
3. The application selects the corresponding typing text.
4. The selected text is displayed to the user.
5. The timer starts when the user begins typing.
6. The application checks the user's input against the selected text.
7. Correct and incorrect characters are highlighted using different colors.
8. The user submits the completed typing test.
9. The application calculates WPM, CPM, time taken, word accuracy, and character accuracy.
10. The results are displayed on the screen.