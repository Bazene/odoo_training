/** @odoo-module */
import { registry } from "@web/core/registry";
import { Component } from "@odoo/owl";

class MyClientAction extends Component {}
MyClientAction.template = "clientaction";

// Register the action in the registry
registry.category("actions").add("estate.MyClientAction", MyClientAction);
