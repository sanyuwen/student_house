[ACID (Atomicity, Consistency, Isolation, Durability)]

A: 
either all of the transaction succeeds or none of it does

C: 
all data will be consistent. 
All data will be valid according to all defined rules, including any constraints, cascades, 
and triggers that have been applied on the database

I:
all transactions will occur in isolation. 
No transaction will be affected by any other transaction. 
So a transaction cannot read data from any other transaction that has not yet completed

D:
once a transaction is committed, it will remain in the system – 
even if there’s a system crash immediately following the transaction. 
Any changes from the transaction must be stored permanently. 
If the system tells the user that the transaction has succeeded, the transaction must have, in fact, succeeded.


[Optimistic concurrency control transactions involve these phases:]

Begin: Record a timestamp marking the transaction's beginning.
Modify: Read database values, and tentatively write changes.
Validate: Check whether other transactions have modified data that this transaction has used (read or written). This includes transactions that completed after this transaction's start time, and optionally, transactions that are still active at validation time.
Commit/Rollback: If there is no conflict, make all changes take effect. If there is a conflict, resolve it, typically by aborting the transaction, although other resolution schemes are possible. Care must be taken to avoid a time-of-check to time-of-use bug, particularly if this phase and the previous one are not performed as a single atomic operation.

