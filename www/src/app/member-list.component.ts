import { Component, OnInit } from '@angular/core';
import { Member } from './member';
import { MemberService } from './member.service';

@Component({
  moduleId: module.id,
  selector: 'member-list',
  templateUrl: 'member-list.component.html',
  styleUrls: ['member-list.component.css'],
})
export class MemberListComponent implements OnInit {
  members: Member[];
  errorMessage: string;
  loading: boolean;

  constructor(private memberService: MemberService) {}

  getMembers(): void {
    this.memberService.getMembers()
                      .subscribe(
                        members => {this.members = members; this.loading = false;},
                        error => this.errorMessage = <any>error
                      );
  }

  ngOnInit(): void {
    this.loading = true;
    this.getMembers();
  }
}
