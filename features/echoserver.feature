Feature: Echo server
    Implement a server that echos back the messages it receives

    Scenario: Echo server for "Hello, world!"
        Given the string Hello, world!
        When I call echo_client
        Then I see the output Hello, world!