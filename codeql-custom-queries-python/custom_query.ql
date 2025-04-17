import python

/**
 * This query finds all functions named "myFunction".
 */
from Function f
where f.getName() = "myFunction"
select f, "This function is called myFunction."
