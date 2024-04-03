/**
 * This code was generated by v0 by Vercel.
 * @see https://v0.dev/t/JYQTaSpvwcc
 */
import { SelectValue, SelectTrigger, SelectItem, SelectGroup, SelectContent, Select } from "@/components/ui/select"
import { TableHead, TableRow, TableHeader, TableCell, TableBody, Table } from "@/components/ui/table"

export function LogTable() {
  return (
    <Table>
      <TableHeader>
        <TableRow>
          <TableHead className="w-[180px]">
            <Select>
              <SelectTrigger className="w-[180px]">
                <SelectValue placeholder="Filter Date/Time" />
              </SelectTrigger>
              <SelectContent>
                <SelectGroup>
                  <SelectItem value="date-asc">Date Ascending</SelectItem>
                  <SelectItem value="date-desc">Date Descending</SelectItem>
                </SelectGroup>
              </SelectContent>
            </Select>
          </TableHead>
          <TableHead>
            <Select>
              <SelectTrigger>
                <SelectValue placeholder="Filter Event Type" />
              </SelectTrigger>
              <SelectContent>
                <SelectGroup>
                  <SelectItem value="access-control">Access Control</SelectItem>
                  <SelectItem value="malware">Malware Detection</SelectItem>
                  <SelectItem value="firewall">Firewall Alert</SelectItem>
                  <SelectItem value="phishing">Phishing Attempt</SelectItem>
                  <SelectItem value="ddos">DDoS Attack</SelectItem>
                </SelectGroup>
              </SelectContent>
            </Select>
          </TableHead>
          <TableHead>
            <Select>
              <SelectTrigger>
                <SelectValue placeholder="Filter Source IP" />
              </SelectTrigger>
              <SelectContent>
                <SelectGroup>
                  <SelectItem value="ip-1">192.168.1.102</SelectItem>
                  <SelectItem value="ip-2">192.168.1.115</SelectItem>
                  <SelectItem value="ip-3">192.168.1.130</SelectItem>
                  <SelectItem value="ip-4">192.168.1.142</SelectItem>
                  <SelectItem value="ip-5">192.168.1.175</SelectItem>
                </SelectGroup>
              </SelectContent>
            </Select>
          </TableHead>
          <TableHead>
            <Select>
              <SelectTrigger>
                <SelectValue placeholder="Filter Destination IP" />
              </SelectTrigger>
              <SelectContent>
                <SelectGroup>
                  <SelectItem value="dest-ip-1">10.23.145.12</SelectItem>
                  <SelectItem value="dest-ip-2">10.23.145.29</SelectItem>
                  <SelectItem value="dest-ip-3">10.23.145.42</SelectItem>
                  <SelectItem value="dest-ip-4">10.23.145.66</SelectItem>
                  <SelectItem value="dest-ip-5">10.23.145.89</SelectItem>
                </SelectGroup>
              </SelectContent>
            </Select>
          </TableHead>
          <TableHead>
            <Select>
              <SelectTrigger>
                <SelectValue placeholder="Filter Severity" />
              </SelectTrigger>
              <SelectContent>
                <SelectGroup>
                  <SelectItem value="severity-high">High</SelectItem>
                  <SelectItem value="severity-medium">Medium</SelectItem>
                  <SelectItem value="severity-low">Low</SelectItem>
                </SelectGroup>
              </SelectContent>
            </Select>
          </TableHead>
          <TableHead>
            <Select>
              <SelectTrigger>
                <SelectValue placeholder="Filter Description" />
              </SelectTrigger>
              <SelectContent>
                <SelectGroup>
                  <SelectItem value="desc-1">Unauthorized access attempt to sensitive files.</SelectItem>
                  <SelectItem value="desc-2">Malware detected in the system. Quarantine initiated.</SelectItem>
                  <SelectItem value="desc-3">Firewall detected suspicious traffic. Investigation initiated.</SelectItem>
                  <SelectItem value="desc-4">Users received phishing emails. Awareness campaign initiated.</SelectItem>
                  <SelectItem value="desc-5">
                    Massive incoming traffic detected. DDoS mitigation in progress.
                  </SelectItem>
                </SelectGroup>
              </SelectContent>
            </Select>
          </TableHead>
        </TableRow>
      </TableHeader>
      <TableBody>
        <TableRow>
          <TableCell className="font-medium">2023-08-15 10:23:45</TableCell>
          <TableCell>Access Control Violation</TableCell>
          <TableCell>192.168.1.102</TableCell>
          <TableCell>10.23.145.12</TableCell>
          <TableCell className="text-center">High</TableCell>
          <TableCell>Unauthorized access attempt to sensitive files.</TableCell>
        </TableRow>
        <TableRow>
          <TableCell className="font-medium">2023-08-15 12:45:32</TableCell>
          <TableCell>Malware Detection</TableCell>
          <TableCell>192.168.1.115</TableCell>
          <TableCell>10.23.145.29</TableCell>
          <TableCell className="text-center">High</TableCell>
          <TableCell>Malware detected in the system. Quarantine initiated.</TableCell>
        </TableRow>
        <TableRow>
          <TableCell className="font-medium">2023-08-15 15:18:21</TableCell>
          <TableCell>Firewall Alert</TableCell>
          <TableCell>192.168.1.130</TableCell>
          <TableCell>10.23.145.42</TableCell>
          <TableCell className="text-center">Medium</TableCell>
          <TableCell>Firewall detected suspicious traffic. Investigation initiated.</TableCell>
        </TableRow>
        <TableRow>
          <TableCell className="font-medium">2023-08-15 17:39:54</TableCell>
          <TableCell>Phishing Attempt</TableCell>
          <TableCell>192.168.1.142</TableCell>
          <TableCell>10.23.145.66</TableCell>
          <TableCell className="text-center">Low</TableCell>
          <TableCell>Users received phishing emails. Awareness campaign initiated.</TableCell>
        </TableRow>
        <TableRow>
          <TableCell className="font-medium">2023-08-15 19:58:12</TableCell>
          <TableCell>DDoS Attack</TableCell>
          <TableCell>192.168.1.175</TableCell>
          <TableCell>10.23.145.89</TableCell>
          <TableCell className="text-center">High</TableCell>
          <TableCell>Massive incoming traffic detected. DDoS mitigation in progress.</TableCell>
        </TableRow>
      </TableBody>
    </Table>
  )
}