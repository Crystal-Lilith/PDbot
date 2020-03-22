class Command
    constructor: (opts={}, @execute) ->
        @name = opts.name or null
        @required_roles = opts.required_roles or []
        @required_perms = opts.required_perms or []
        @desc = opts.desc or opts.description or 'No description provided for this command.'

