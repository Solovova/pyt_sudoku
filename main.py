from solve.sudSolveOld import SudSolveOld
import json

from solver.schema.sudSchema import SudSchema
from solver.schema.sudSchemaJson import SudSchemaJson


def main():
    # sud_solve: SudSolveOld = SudSolveOld()
    # sud_solve.solve()

    schema_json: SudSchemaJson = SudSchemaJson()
    schema: SudSchema = SudSchema(schema_json)
    schema.print_compact()


if __name__ == '__main__':
    main()
