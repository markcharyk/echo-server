Feature: Echo server
    Implement a server that echos back the messages it receives

    Scenario Outline: Echo server for strings
        Given the string: <input>
        When I call echo_client
        Then I see the output: <output>

    Examples:
        | input                                                                                | output                                                                              |
        | Hello, world                                                                     | Hello, world                                                                      |
        | A string longer than 32 characters because I type a lot | A string longer than 32 characters because I type a lot |
        | ABCDEFGHIJKLMNOPQRSTUVWXYZ123456                    | ABCDEFGHIJKLMNOPQRSTUVWXYZ123456                    |