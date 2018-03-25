Feature: Group adding feature
  Description

  Scenario Outline: Add new group
    Given a group list
    Given data for new group with <name>, <header>, <footer>
    When I add a new group with this data
    Then correct message is displayed
    Then a new group list is equal to the old group with this new group

    Examples:
    | name  | header  | footer  |
    | fdfdf | ewewewe | dsdsdsd |
    | 32323 | #@#@#@# | 3232323 |
    | fd323 | 3ddd#@# | 4543333 |

