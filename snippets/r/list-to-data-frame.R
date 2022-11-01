# Convert a list to a data frame.

capitals <- list(
    countries = c("England", "Scotland", "Wales"),
    city = c("London", "Edinburgh", "Cardiff")
)

# Convert to a data frame.
#
as.data.frame(capitals)
data.frame(capitals)

# Convert to a tibble.
#
tibble::as_tibble(capitals)

