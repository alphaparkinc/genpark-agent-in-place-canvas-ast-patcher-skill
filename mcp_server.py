import sys
import json
from client import InPlaceCanvasASTPatcher

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "apply_patch",
                        "description": "Applies a surgical field patch to an AST canvas node.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "canvas_doc": {"type": "object"},
                                "node_id": {"type": "string"},
                                "field_path": {"type": "string"},
                                "new_value": {"type": "string"}
                            }
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        args = params.get("arguments", {})
        patcher = InPlaceCanvasASTPatcher()
        res = patcher.apply_patch(
            args.get("canvas_doc", {}),
            args.get("node_id", "1"),
            args.get("field_path", "headline"),
            args.get("new_value", "")
        )
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "content": [{"type": "text", "text": json.dumps(res, indent=2)}]
            }
        }
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    patcher = InPlaceCanvasASTPatcher()
    print(json.dumps(patcher.apply_patch({"slides": [{"slide_index": 1, "headline": "Title"}]}, "1", "headline", "New"), indent=2))

if __name__ == "__main__":
    main()
