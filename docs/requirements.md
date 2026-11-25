Software Design and Architecture
PayLink Year Work Project

•Problem summery:

PayLink is a digital bill payment and e-wallet system in Egypt that allows customers to pay their utility bills, such as electricity, water, mobile, and internet bills, using their digital wallets through a mobile application or authorized agents.
The main problem PayLink aims to solve is making bill payments easier, faster, and more reliable without requiring customers to visit utility offices or wait in long queues.
The system allows customers to check their bills, view the required amount and service fees, and pay directly from their wallet. It also supports agents who can make payments on behalf of customers and earn commissions.
However, handling digital payments comes with important challenges. The system must prevent duplicate payments, incorrect charges, and negative wallet balances. It must also handle failed transactions, delayed biller responses, refunds, and payment confirmations correctly.
PayLink needs to integrate with different biller companies that use different communication protocols and payment methods. Therefore, the system should be flexible and easy to extend when adding new billers without changing existing modules.
The system must also provide secure wallet management, accurate transaction records, fraud detection, customer notifications, and daily reconciliation to ensure that all payments are correctly recorded.
The main goal is to build a reliable, secure, and scalable backend system that handles customer wallets and bill payments accurately, even when errors or unexpected situations occur.



•Stakeholders:

The main stakeholders involved in the PayLink system are:
Stakeholders:

1. Customers
- Register, add money to their wallets, and pay utility bills.
- View payment history and receive notifications.

2. Agents
- Help customers pay bills through PayLink terminals.
- Receive commissions for successful payments.

3. Biller Companies
- Provide bill information and receive payments.
- Send payment confirmations and daily settlement files.

4. PayLink Management
- Manage business operations and monitor transactions, fees, and commissions.
- Ensure customer satisfaction and business profitability.

5. Engineering and Development Team
- Develop and maintain the backend system.
- Integrate billers and ensure system reliability and security.


•Functional Requirements – User Stories:

FR-1: Customer Registration
Priority: Must
User Story:
As a customer, I want to register for a PayLink account with basic verification, so that I can use the system's wallet and payment services.
Acceptance Criteria:
•	Given that I am a new user, When I submit valid registration information, Then the system creates my account with a basic verification level.
•	Given that I provide invalid or incomplete information, When I submit the registration form, Then the system rejects the registration and displays an error message.
FR-2: Upgrade Verification Level
Priority: Should
User Story:
As a customer, I want to upgrade my account to a verified level, so that I can have higher daily payment limits.
Acceptance Criteria:
•	Given that I have a basic account, When my verification is successfully approved, Then my account level changes to verified.
•	Given that my account is verified, When I make a payment, Then the system applies the verified daily limit of 30,000 EGP.
FR-3: View Wallet Balance and Transaction History
Priority: Must
User Story:
As a customer, I want to view my available balance, held balance, and transaction history, so that I can track my money and payments.
Acceptance Criteria:
•	Given that I am logged in, When I open my wallet, Then the system displays my available and held balances.
•	Given that I have previous transactions, When I open my transaction history, Then the system displays my recorded transactions.

FR-4: Wallet Top-up
Priority: Must
User Story:
As a customer, I want to add money to my wallet using a simulated card or agent cash, so that I can pay my bills.
Acceptance Criteria:
•	Given that I have a valid top-up request, When the card or agent cash top-up succeeds, Then the system adds the amount to my wallet.
•	Given that a top-up fails, When the transaction is processed, Then the system does not increase my wallet balance.
FR-5: Ledger Entries
Priority: Must
User Story:
As a system, I want every wallet balance change to create a ledger entry, so that all financial movements are recorded accurately.
Acceptance Criteria:
•	Given that a wallet balance changes, When the transaction is completed, Then the system creates a corresponding ledger entry.
•	Given that a wallet balance is requested, When the system calculates it, Then the balance is calculated from ledger entries instead of being overwritten directly.
FR-6: Manage Billers and Services
Priority: Must
User Story:
As an admin, I want to add, edit, and disable billers and their services, so that I can manage the available payment providers.
Acceptance Criteria:
•	Given that I am an admin, When I add a new biller with valid information, Then the system saves the biller.
•	Given that a biller already exists, When I edit its information or disable it, Then the system updates its status or details.
FR-7: View Available Billers
Priority: Must
User Story:
As a customer, I want to see the available billers and their required input fields, so that I can provide the correct information for my bill.
Acceptance Criteria:
•	Given that I open the bill payment section, When I request the biller list, Then the system displays the available billers.
•	Given that I select a biller, When I open its service details, Then the system displays the required input fields, such as meter number or phone number.
FR-8: Bill Inquiry
Priority: Must
User Story:
As a customer, I want to check my bill before paying, so that I know the bill amount, service fee, and total amount.
Acceptance Criteria:
•	Given that I select a biller and enter valid required information, When I request a bill inquiry, Then the system retrieves and displays the bill amount.
•	Given that the bill amount is retrieved, When the service fee is calculated, Then the system displays the bill amount, fee, and total before payment.
FR-9: Pay a Bill
Priority: Must
User Story:
As a customer, I want to pay a bill using my PayLink wallet, so that I can complete bill payments without visiting the biller's office.
Acceptance Criteria:
•	Given that I have enough available wallet balance, When I confirm a valid bill payment, Then the system starts processing the payment.
•	Given that the payment is confirmed by the biller, When the system receives the confirmation, Then the payment is marked as Completed and the final amount is charged.
FR-10: Prevent Duplicate Payment Requests
Priority: Must
User Story:
As a customer, I want repeated payment requests with the same idempotency key to return the original result, so that I am not charged twice.
Acceptance Criteria:
•	Given that a payment request has already been processed with a specific idempotency key, When the same request is submitted again with that key, Then the system returns the original result without creating another payment or charge.
FR-11: Payment Life Cycle
Priority: Must
User Story:
As a system, I want every payment to follow the defined payment life cycle, so that payment statuses remain valid and consistent.
Acceptance Criteria:
•	Given that a payment is Initiated and fraud checks pass with sufficient funds, When processing continues, Then its status changes to FundsHeld.
•	Given that a payment is SentToBiller, When the biller confirms it, Then its status changes to Completed.
•	Given that a payment is SentToBiller, When the biller refuses it, Then its status changes to Failed.
•	Given that a payment is SentToBiller, When the biller does not respond within the timeout, Then its status changes to Unknown.
•	Given that a payment is in a final state, When another invalid status transition is requested, Then the system rejects that transition.
FR-12: Hold and Release Funds
Priority: Must
User Story:
As a customer, I want the payment amount to be held before contacting the biller and released if payment fails, so that my wallet balance remains accurate.
Acceptance Criteria:
•	Given that I have enough available balance, When a payment passes the required checks, Then the system moves the total amount from available balance to held balance before calling the biller.
•	Given that the biller refuses the payment, When the payment becomes Failed, Then the system releases the held amount back to my available balance.
FR-13: Handle Payment Timeouts
Priority: Must
User Story:
As a customer, I want delayed payments to be marked as Unknown and checked again, so that I do not lose money when the biller response is delayed.
Acceptance Criteria:
•	Given that the biller does not respond within 10 seconds, When the timeout occurs, Then the payment becomes Unknown and the held funds remain reserved.
•	Given that a payment is Unknown, When the retry schedule is triggered, Then the system re-queries the biller after 1, 5, and 15 minutes, up to 3 retries.
FR-14: Handle Asynchronous Callbacks
Priority: Must
User Story:
As a system, I want to receive asynchronous callbacks from TopUpNet and ignore duplicate callbacks, so that mobile top-up payments are completed only once.
Acceptance Criteria:
•	Given that a TopUpNet payment is waiting for confirmation, When a valid success callback is received, Then the system completes the payment.
•	Given that the same callback is received more than once, When the system processes the duplicate callback, Then it ignores the duplicate and logs it without completing the payment again.
FR-15: Support Multiple Billers
Priority: Must
User Story:
As a customer, I want to pay through different billers, so that I can use PayLink for electricity, water, and mobile top-ups.
Acceptance Criteria:
•	Given that ElectroCo, AquaCo, and TopUpNet are configured, When I select one of their services, Then the system communicates with the selected biller.
•	Given that each biller uses a different communication format, When a payment or inquiry is sent, Then the system handles the biller's required protocol and format through its integration.
FR-16: Calculate Service Fees
Priority: Must
User Story:
As a customer, I want service fees to be calculated according to the biller and promotion rules, so that I know the correct total amount before paying.
Acceptance Criteria:
•	Given that I am paying an electricity or water bill, When the fee is calculated, Then the system applies the fixed fee of 2.50 EGP.
•	Given that I am making a mobile top-up, When the fee is calculated, Then the system applies 1.5% of the amount with a minimum fee of 1 EGP.
•	Given that I am paying an internet bill, When the fee is calculated, Then the system applies 2 EGP for amounts up to 200 EGP and 4 EGP for amounts above 200 EGP.
•	Given that an active promotion applies to the selected biller, When the fee is calculated during the promotion period, Then the system applies a zero service fee.
FR-17: Agent Payments and Commission
Priority: Should
User Story:
As an agent, I want to pay bills on behalf of customers, so that I can help them complete payments and earn commissions.
Acceptance Criteria:
•	Given that I am an authorized agent, When I submit a valid payment on behalf of a customer, Then the system processes the payment.
•	Given that the agent's payment is completed, When the commission is calculated, Then the system credits 40% of the service fee to the agent's wallet.
FR-18: Payment Amount and Daily Limits
Priority: Must
User Story:
As a system, I want to reject payments that exceed the allowed single-payment or daily limits, so that account payment limits are enforced.
Acceptance Criteria:
•	Given that a customer submits a payment below 5 EGP or above 10,000 EGP, When the system validates the amount, Then the payment is rejected with a clear reason.
•	Given that a basic customer exceeds the daily limit of 5,000 EGP, When another payment is submitted, Then the system rejects it with a clear reason.
•	Given that a verified customer exceeds the daily limit of 30,000 EGP, When another payment is submitted, Then the system rejects it with a clear reason.
FR-19: Payment Velocity Check
Priority: Should
User Story:
As a system, I want to block accounts that make more than 5 payments within 60 seconds, so that suspicious payment activity can be prevented.
Acceptance Criteria:
•	Given that an account makes more than 5 payments within 60 seconds, When the system checks its payment activity, Then the account is blocked for 10 minutes.
•	Given that the 10-minute blocking period has ended, When the customer attempts another payment, Then the system allows the request if all other checks pass.
FR-20: Search Payment Details
Priority: Must
User Story:
As a support employee, I want to search for a payment using its reference number, so that I can investigate customer payment issues.
Acceptance Criteria:
•	Given that I have a valid payment reference number, When I search for the payment, Then the system displays its details and full history.
•	Given that the reference number does not exist, When I search for it, Then the system displays a not-found message.
FR-21: Block and Unblock Accounts
Priority: Should
User Story:
As a support employee, I want to block and unblock customer accounts, so that I can handle suspicious or problematic accounts.
Acceptance Criteria:
•	Given that I have the required support permissions, When I block a customer account, Then the system prevents that account from making payments.
•	Given that an account is blocked, When I unblock it, Then the system allows the account to make payments again if all other checks pass.
FR-22: Payment Notifications
Priority: Must
User Story:
As a customer, I want to receive SMS and push notifications when a payment succeeds or fails, so that I know the result of my transaction.
Acceptance Criteria:
•	Given that my payment is completed, When the system confirms the payment, Then it sends me an SMS and a push notification.
•	Given that my payment fails, When the system confirms the failure, Then it sends me an SMS and a push notification explaining the failure.
FR-23: Retry Failed Notifications
Priority: Should
User Story:
As a system, I want to retry failed SMS or email notifications, so that customers have a better chance of receiving payment updates.
Acceptance Criteria:
•	Given that an SMS or email notification fails, When the system detects the failure, Then it retries sending the notification up to 3 times.
•	Given that all 3 retries fail, When the retry process ends, Then the notification is marked as undelivered.
•	Given that the notification provider is unavailable, When a payment completes, Then the payment itself remains completed and is not cancelled because of the notification failure.
FR-24: Update Fees and Limits
Priority: Should
User Story:
As an admin, I want to edit fee and limit values without redeploying the system, so that business rules can be updated easily.
Acceptance Criteria:
•	Given that I am an authorized admin, When I update a fee or limit value, Then the system saves the new configuration.
•	Given that a new fee or limit configuration is saved, When a new payment is processed, Then the system uses the updated values without requiring redeployment.
FR-25: Audit Log
Priority: Must
User Story:
As a company administrator, I want every money movement and admin action to be recorded in an audit log, so that financial operations and administrative changes can be traced.
Acceptance Criteria:
•	Given that a money movement occurs, When the transaction is processed, Then the system records the action in the audit log.
•	Given that an admin performs an action, When the action is completed, Then the system records the action and its details in the audit log.
FR-26: Daily Reconciliation Report
Priority: Should
User Story:
As a support employee, I want the system to compare PayLink transactions with the biller's settlement file, so that I can identify payment differences.
Acceptance Criteria:
•	Given that a biller provides a daily settlement file, When the reconciliation process runs, Then the system compares the file with PayLink's payment records.
•	Given that a difference is found, When reconciliation is completed, Then the system flags the difference in a report for support to review.
FR-27: Request a Refund
Priority: Could
User Story:
As a customer, I want to request a refund for a completed payment, so that I can ask for my money back when necessary.
Acceptance Criteria:
•	Given that I have a completed payment, When I submit a refund request, Then the system records the request for support approval.
•	Given that support approves the refund request, When the refund is processed, Then the system returns the approved amount to my wallet and records the transaction.
FR-28: View Daily Business Totals
Priority: Could
User Story:
As an admin, I want to view daily payment totals, fees earned, commissions paid, and failures per biller, so that I can monitor PayLink's business performance.
Acceptance Criteria:
•	Given that daily transactions have been recorded, When I open the daily summary, Then the system displays the total number of payments, fees earned, and commissions paid.
•	Given that payments have been made through different billers, When I view the daily summary, Then the system displays the number of failures for each biller.


o	Non functional req 

Quality 	Target
Correctness
(must)	Zero double charges and zero negative balances in the concurrency and duplicate tests
Performance
(should)	100 payments per second sustained for 1 minute against the mock billers
Resilience
(must)	A biller outage does not stop payments to other billers
Modifiability
(should)	Adding a biller touches only the Biller Integration module and configuration
Auditability
(must)	100% of money movements have an audit record with who, when and why
Testability
(must)	At least 70% line coverage on domain logic, measured in CI


•	Questions, Ambiguities, and Decisions
No.	Question / Ambiguity	Decision Made
1	What happens if a customer sends the same payment request twice because of a network problem?	The system uses an idempotency key to ensure that the payment is processed only once. Repeated requests return the original result without creating another charge.
2	What happens if the biller does not respond within 10 seconds?	The payment status changes to Unknown, and the money remains held in the customer's wallet until the system confirms whether the biller received the payment.
3	What happens if two payments arrive at the same time and the wallet balance is enough for only one?	The system must allow only one payment to succeed and reject the other, ensuring that the wallet balance never becomes negative.
4	What happens if the biller sends the same success callback more than once?	The system processes the first valid callback and ignores and logs duplicate callbacks to prevent completing or charging the same payment more than once.
5	How can a new biller be added without affecting the existing system?	A separate integration adapter and configuration are added for the new biller. Existing modules remain unchanged.

Conclusion
These decisions focus on preventing financial errors, handling unexpected failures, maintaining wallet consistency, and making the system easy to extend.
