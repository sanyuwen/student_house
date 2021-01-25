### unit of work
A Unit of Work keeps track of everything you do during a business transaction that can affect the database. 
When you're done, it figures out everything that needs to be done to alter the database as a result of your work.

### in EF core
Each context instance has a _ChangeTracker_ that is responsible for keeping track of changes that need to be written to the database.

### lifetime of a DbContext
DbContext is designed to represent a shot-lived unit-of-work.
1. Create the DbContext instance
2. track some entities
3. make some changes to the entities
4. SaveChanges to update the database
5. Dispose the DbContext instance

### Entity instances
1. become tracked when:
    * returned from a query executed against the database
    * explicitly attached to DbContext by _Add_, _Attach_, _Update_ or similar methods
    * detected as new entities connected to existing tracked entities
2. are no longer tracked when:
    * DbContext is disposed
    * the change tracker is cleared
    * entities are explicitly detached

### entity states
|Entity state|Tracked by DbContext|Exists in database|Properties modified|Action on SaveChanges|
|----|----|----|----|----|
|Detached|No|-|-|-|
|Added|Yes|No|-|Insert|
|Unchanged|Yes|Yes|No|-|
|Modified|Yes|Yes|Yes|Update|
|Deleted|Yes|Yes|-|Delete|

