# Created by slkpd at 27-10-2022
Feature: Verify whether cricket player profile details were added and whether we are able to get the players data using PlayerAPI
  # Enter feature description here
  @API
  Scenario: Verify Players profiles adding API functionality
    Given The player details which needs to be added to database
    When We execute the Insert PostAPI method
    Then Profile is successfully inserted
    And  status code of response should be 200

  @API
  Scenario Outline: Verify Players profiles adding API functionality
    Given The player details <player> and <test> and <odi> and <t20> which needs to be added to database
    When We execute the Insert PostAPI method
    Then Profile is successfully inserted
    Examples:
      | player | test | odi | t20 |
      | Iyer   | 5    | 35  | 35  |
      | Ishan Kishan   | 0  | 15  | 35  |

