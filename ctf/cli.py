import argparse


def parse_args():
    parser = argparse.ArgumentParser()

    common_parser = argparse.ArgumentParser(add_help=False)

    common_parser.add_argument("--base", dest="base_branch", default="master",
                               help=("Base branch against which we want to "
                                     "compare, default is \"master\" branch"))
    common_parser.add_argument("--repository", dest="repository_path",
                               help=("Path to ComplianceAsCode repository. "
                                     "If not provided, the repository will be "
                                     "cloned into /tmp folder."))
    common_parser.add_argument("--remote_repo", dest="remote_repo",
                               default="https://github.com/ggbecker/content",
                               help=("Remote repository for pulling, updating "
                                     "and finding branches (Pull requests). Default "
                                     "is https://github.com/ComplianceAsCode/content."))
    common_parser.add_argument("--local", dest="local", default=False,
                               action="store_true", help="Do not pull from remote, "
                               "use local branches. Mainly for testing purposes.")
    common_parser.add_argument("--verbose", dest="verbose", default=False,
                               action="store_true", help="Increase verbose level of "
                               "logging to DEBUG level. Default level is INFO")
    common_parser.add_argument("--output-tests", dest="output_tests", default=False,
                               action="store_true", help="Output only list of tests. "
                               "Completely turns off all other outputs.")
    common_parser.add_argument("--output-format", dest="output_format", default="raw",
                               action="store", choices=["raw", "markdown"],
                               help="Output format.")

    parser.set_defaults(pr_number=None, branch=None)

    subparsers = parser.add_subparsers(dest="subcommand",
                                       help="Subcommands: pr, branch")
    subparsers.required = True

    parser_pr = subparsers.add_parser("pr", parents=[common_parser],
                                      help=("Compare base against selected "
                                            "pull request"))
    parser_pr.add_argument("pr_number", metavar="PR_NUMBER", default=None,
                           help=("Pull request number, which we want compare "
                                 "against base"))

    parser_branch = subparsers.add_parser("branch", parents=[common_parser],
                                          help=("Compare base against selected branch"))
    parser_branch.add_argument("branch", metavar="BRANCH_NAME", default=None,
                               help=("Branch, which we want compare "
                                     "against base"))

    options = parser.parse_args()

    return options
